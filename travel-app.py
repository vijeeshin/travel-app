from datetime import date

import streamlit as st

st.title("AI Traveller APP")

Destination =st.text_input("Enter Destination:")
Travel_date=st.date_input("Enter Travel Date:")
budget=st.number_input("Enter Budget: ", min_value=0.0)

travel_type_options = ["Solo", "Family", "Couple", "Business"]
travel_type=st.selectbox(
    "Travel Type",
    travel_type_options
    )

interest_options = ["Beach", "Temple", "Adventure", "Nature"]
interest =st.multiselect(
    "Interest",
    interest_options
)

if st.button("Submit"):
    errors = {}
    if not Destination.strip():
        errors["Destination"] = "Enter a destination."
    if Travel_date <= date.today():
        errors["Travel Date"] = "Choose a travel date in the future."
    if budget <= 0:
        errors["Budget"] = "Budget must be greater than zero."
    if travel_type not in travel_type_options:
        errors["Travel Type"] = "Choose a valid travel type."
    if not interest:
        errors["Interest"] = "Select at least one interest."
    elif any(item not in interest_options for item in interest):
        errors["Interest"] = "Choose valid interests."

    if errors:
      for field, message in errors.items():
        st.error(f"{field}: {message}")
      st.stop()

    st.write("Budget Analysis")

    if budget < 10000:
      budget_category="Low Budget"
      hotel_type="Budget Hotel"

    elif budget< 30000:

      budget_category="Medium Budget"
      hotel_type="3-Star Hotel"

    elif budget < 60000:

      budget_category = "Premium Budget"
      hotel_type = "4-Star Hotel"

    else:

      budget_category="Luxury  Budget"
      hotel_type="5-Star Resort"

    st.write(f"Budget Category : {budget_category}")
    st.write(f"Recommended Stay : {hotel_type}")


    st.write("## Travel Recommendation ###")

    if travel_type == "Solo":
        st.info("Explore local attractions and backpacking routes.")

    elif travel_type == "Family":
        st.info("Choose family-friendly hotels and sightseeing packages.")

    elif travel_type == "Couple":
        st.info("Romantic resorts and candle-light dinners recommended.")

    elif travel_type == "Business":
        st.info("Stay near business districts with conference facilities.")

    score=0

    for item in interest:

      if item=="Adventure":
        score+=20   # score=score+20

      elif item=="Nature":
        score+=15

      else:
        score+=10 #score=+10

    if budget> 30000:
      score+=25

    if travel_type in ["Family","Couple"]:
      score+=25


    st.write(f"""
    ###Travel Summary

    Destination \t : {Destination}

    Travel Date \t : {Travel_date}

    Budgent \t : ₹{budget}

    Travel_type \t : {travel_type}

    Interst \t :{interest}

    Final Score: {score}

    """)
    st.balloons()

print("Thank you")
