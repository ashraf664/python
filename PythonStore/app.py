import json

import streamlit as st

from inventory import Inventory
from storage import ProductStorage


st.set_page_config(page_title="إدارة المتجر", page_icon="🛍️", layout="wide")

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
    }
    [data-testid="stMarkdown"], [data-testid="stWidgetLabel"],
    [data-testid="stMetric"], [data-testid="stDataFrame"] {
        text-align: right;
    }
    input, textarea {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🛍️ إدارة المتجر")
st.caption("إدارة المنتجات والمخزون والمبيعات. تُحفظ التغييرات في ملف المنتجات الحالي.")

if notice := st.session_state.pop("store_notice", None):
    st.success(notice)

storage = ProductStorage()
try:
    inventory = Inventory(storage.load_products())
except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
    st.error(f"تعذر تحميل المنتجات من ملف الحفظ: {error}")
    st.stop()


def save_and_refresh(success_message):
    try:
        storage.save_products(inventory.products)
    except OSError as error:
        st.error(f"تعذر حفظ التغييرات: {error}")
        return

    st.session_state["store_notice"] = success_message
    st.rerun()


def product_table(products):
    if not products:
        st.info("لا توجد منتجات لعرضها.")
        return

    rows = [
        {
            "رقم المنتج": product.product_id,
            "اسم المنتج": product.name,
            "السعر": product.price,
            "الكمية المتوفرة": product.quantity,
        }
        for product in products
    ]
    st.dataframe(rows, width="stretch", hide_index=True)


tab_products, tab_search, tab_inventory, tab_sales = st.tabs(
    ["المنتجات", "البحث", "إدارة المخزون", "المبيعات"]
)

with tab_products:
    st.subheader("المنتجات في المتجر")
    total_products = len(inventory.products)
    total_units = sum(product.quantity for product in inventory.products)
    first_metric, second_metric = st.columns(2)
    first_metric.metric("عدد المنتجات", total_products)
    second_metric.metric("إجمالي الوحدات في المخزون", total_units)
    product_table(inventory.products)

    with st.form("add_product_form"):
        st.subheader("إضافة منتج")
        name = st.text_input("اسم المنتج")
        price = st.number_input("السعر", min_value=0.01, value=1.0, step=1.0)
        quantity = st.number_input(
            "الكمية الابتدائية", min_value=0, value=0, step=1
        )
        add_submitted = st.form_submit_button("إضافة المنتج")

    if add_submitted:
        try:
            product = inventory.add_product(name, price, quantity)
        except ValueError as error:
            st.error(str(error))
        else:
            save_and_refresh(f"تمت إضافة المنتج «{product.name}» بنجاح.")

with tab_search:
    st.subheader("البحث عن منتج")
    search_text = st.text_input("اكتب اسم المنتج أو جزءًا منه")
    matching_products = inventory.search_products(search_text)
    if search_text.strip() and not matching_products:
        st.info("لم يُعثر على منتجات تطابق البحث.")
    else:
        product_table(matching_products)

with tab_inventory:
    st.subheader("تعديل السعر والكمية")
    if not inventory.products:
        st.info("أضف منتجًا أولًا لتتمكن من تعديل المخزون.")
    else:
        product_ids = [product.product_id for product in inventory.products]

        def format_product(product_id):
            product = inventory.get_product(product_id)
            return f"{product.name} (رقم {product.product_id})"

        with st.form("update_product_form"):
            selected_id = st.selectbox(
                "اختر المنتج", product_ids, format_func=format_product
            )
            selected_product = inventory.get_product(selected_id)
            new_price = st.number_input(
                "السعر الجديد",
                min_value=0.01,
                value=float(selected_product.price),
                step=1.0,
            )
            new_quantity = st.number_input(
                "الكمية الجديدة",
                min_value=0,
                value=int(selected_product.quantity),
                step=1,
            )
            update_submitted = st.form_submit_button("حفظ التعديل")

        if update_submitted:
            try:
                inventory.update_product(selected_id, new_price, new_quantity)
            except ValueError as error:
                st.error(str(error))
            else:
                save_and_refresh("تم تحديث بيانات المنتج.")

        st.divider()
        st.subheader("المخزون الحالي")
        product_table(inventory.products)

with tab_sales:
    st.subheader("بيع منتج")
    if not inventory.products:
        st.info("لا توجد منتجات للبيع.")
    else:
        product_ids = [product.product_id for product in inventory.products]

        def format_sale_product(product_id):
            product = inventory.get_product(product_id)
            return (
                f"{product.name} — المتوفر: {product.quantity} "
                f"(رقم {product.product_id})"
            )

        with st.form("sell_product_form"):
            sale_product_id = st.selectbox(
                "اختر المنتج", product_ids, format_func=format_sale_product
            )
            sale_product = inventory.get_product(sale_product_id)
            sale_quantity = st.number_input(
                "كمية البيع",
                min_value=1,
                max_value=max(1, int(sale_product.quantity)),
                value=1,
                step=1,
                disabled=sale_product.quantity == 0,
            )
            if sale_product.quantity == 0:
                st.warning("هذا المنتج غير متوفر حاليًا في المخزون.")
            sell_submitted = st.form_submit_button(
                "تنفيذ البيع", disabled=sale_product.quantity == 0
            )

        if sell_submitted:
            try:
                total = inventory.sell_product(sale_product_id, sale_quantity)
            except ValueError as error:
                st.error(str(error))
            else:
                save_and_refresh(f"تم البيع بنجاح. إجمالي العملية: {total:.2f}.")

        st.divider()
        st.subheader("المخزون المتاح")
        product_table(inventory.products)
