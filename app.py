import streamlit as st
import pandas as pd
from inventory import add_product, get_products, update_stock, delete_stock

st.set_page_config(page_title="Beternovik's Inventory", page_icon="👖", layout="wide")
st.title("Beternovik's Inventory Management System")

# Sidebar menu
menu = ["Dashboard", "Add Product", "Update Stock", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# 1. Dashboard (READ)
if choice == "Dashboard":
    st.subheader("Current Stock Overview")
    products = get_products()

    if products:
        df = pd.DataFrame(products, columns=['ID', 'Category', 'Color', 'Size', 'Cost', 'Price', 'Stock', 'Status'])

        # Displaying metrics at the top
        total_stock = df['Stock'].sum()
        total_value = (df['Stock'] * df['Price']).sum()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Items", total_stock)
        col2.metric("Total inventory value", f'${total_value}')
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index('Color')['Stock'])
    else:
        st.info("No products found in the database.")

# 2. Add product (CREATE)
elif choice == "Add Product":
    st.subheader("Add new inventory")

    with st.form("add_form"):
        col1, col2, col3 = st.columns(3)
        cat = col1.selectbox("Category", ["Pantalon", "Empaquetado"])
        color = col2.selectbox("Color", ["Negro", "Gris", "Caqui", "Verde", "Azul", "Hueso", "Dorado", "Transparente"])
        size = col3.selectbox("Size", ["CH", "M", "G", "XL"])

        col4, col5 = st.columns(2)
        cost = col4.number_input("Cost price", min_value=0.0, value=200.0, step=10.0)
        sell = col5.number_input("Sell price", min_value=0.0, value=350.0, step=10.0)
        stock = st.number_input("Current Stock", min_value=1, step=1)

        submitted = st.form_submit_button("Add to Database")

        if submitted:
            add_product(cat, color, size, cost, sell, stock)
            st.success(f'Added {cat} ({color}, {size}) ot inventory!')

# 3. Update stock (UPDATE)
elif choice == "Update Stock":
    st.subheader("Update stock")

    product_id = st.number_input("Product ID", min_value=1)
    new_stock = st.number_input("New Quantity", min_value=0)

    if st.button("Update stock"):
        update_stock(product_id, new_stock)
        st.success(f'Stock for ID: {product_id} updated to {new_stock}')

# 4. Delete (DELETE)
elif choice == "Delete":
    st.subheader("Remove product")
    # Defining a popup window function
    @st.dialog("Confirmation required")
    def confirm_delete(product_id):
        st.write(f'Are you sure you want to delete Prodcut ID: {product_id}')
        
        col1, col2 = st.columns(2)

        if col1.button("Yes, Delete it bro jeje", type="primary"):
            delete_stock(product_id)
            st.success("Prodcut deleted successfully")
            st.rerun() # This reloads the app to close the modal
        if col2.button("NOOO Cancel"):
            st.rerun()
    product_id = st.number_input("Product ID to remove", min_value=1)

    # When we press this button, the popup opens
    if st.button("Delete product"):
        confirm_delete(product_id)

# $ streamlit run app.py