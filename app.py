
import streamlit as st

st.set_page_config(
    page_title="My Diet Analytics",
    page_icon="🥗"
)

st.title("🥗 My Diet Analytics")
st.write("Track your daily nutrition.")

foods = {
    "Apple": {
        "Calories": 95, "Protein": 0.5,
        "Carbs": 25, "Fat": 0.3
    },
    "Banana": {
        "Calories": 105, "Protein": 1.3,
        "Carbs": 27, "Fat": 0.4
    },
    "Roti": {
        "Calories": 120, "Protein": 3,
        "Carbs": 20, "Fat": 3
    },
    "Dal": {
        "Calories": 150, "Protein": 9,
        "Carbs": 22, "Fat": 3
    },
    "Milk": {
        "Calories": 122, "Protein": 8,
        "Carbs": 12, "Fat": 5
    }
}

if "food_log" not in st.session_state:
    st.session_state.food_log = []

st.subheader("Add food")

food_name = st.selectbox(
    "Choose food", list(foods.keys())
)

servings = st.number_input(
    "Number of servings",
    min_value=0.5,
    max_value=10.0,
    value=1.0,
    step=0.5
)

if st.button("Add to my food log"):
    st.session_state.food_log.append({
        "Food": food_name,
        "Servings": servings,
        **{
            key: value * servings
            for key, value in foods[food_name].items()
        }
    })
    st.success(f"Added {food_name}!")

st.subheader("Daily nutrition report")

if st.session_state.food_log:
    totals = {
        nutrient: sum(
            item[nutrient]
            for item in st.session_state.food_log
        )
        for nutrient in [
            "Calories", "Protein", "Carbs", "Fat"
        ]
    }

    col1, col2 = st.columns(2)
    col1.metric(
        "Calories", f"{totals['Calories']:.1f} kcal"
    )
    col2.metric(
        "Protein", f"{totals['Protein']:.1f} g"
    )

    col3, col4 = st.columns(2)
    col3.metric("Carbs", f"{totals['Carbs']:.1f} g")
    col4.metric("Fat", f"{totals['Fat']:.1f} g")

    st.subheader("Foods eaten")
    st.dataframe(st.session_state.food_log)

    if st.button("Clear today's food log"):
        st.session_state.food_log = []
        st.rerun()
else:
    st.info(
        "Add your first food to see your nutrition report."
    )
