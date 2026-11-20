import streamlit as st
from agent.travel_agent import plan_trip

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

st.title("✈️ Agentic AI Travel Planner")
st.write("Plan your journey with AI-powered travel recommendations.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    source = st.text_input("Starting City", "Mumbai")

with col2:
    city = st.text_input("Destination City", "Delhi")

if st.button("🧳 Plan My Trip", use_container_width=True):
    if not source.strip() or not city.strip():
        st.warning("Please enter both cities.")
    else:
        with st.spinner("AI is planning your trip..."):
            try:
                result = plan_trip(city, source)

                st.success("Your trip plan is ready!")

                st.subheader("✈️ Available Flights")
                st.write(result["flights"])

                st.subheader("🏨 Available Hotels")
                st.write(result["hotels"])

                st.subheader("📍 Places to Visit")
                st.write(result["places"])

                st.divider()

                st.subheader("🤖 AI Generated Travel Itinerary")
                st.markdown(result["itinerary"])

            except Exception as e:
                st.error(f"Error: {e}")