import streamlit as st

# Custom CSS for better styling with background color
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg,#E6F4EA,
 0%, #764ba2 10%);
    }
    
    /* Content area background */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 30px;
        padding: 20px;
        background-color : white;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        border: none;
        font-weight: bold;
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Form sections */
    h3 {
        color: #667eea;
        border-bottom: 2px solid #667eea;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    '<h1 class="main-title">Student Registration Form</h1>',
    unsafe_allow_html=True
)

# Create form
with st.form("student_registration_form"):
    st.subheader("Personal Information")
    
    # Name field
    name = st.text_input("Full Name *", placeholder="Enter your full name")
    
    # Email field
    email = st.text_input("Email Address *", placeholder="student@example.com")
    
    # Age field
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age *", min_value=5, max_value=100, value=18)
    with col2:
        gender = st.selectbox("Gender *", ["Select", "Male", "Female", "Other", "Prefer not to say"])
    
    # Contact Information
    st.subheader("Contact Information")
    
    phone = st.text_input("Phone Number", placeholder="+1 (555) 123-4567")
    address = st.text_area("Address", placeholder="Enter your full address")
    
    # Academic Information
    st.subheader("Academic Information")
    
    col3, col4 = st.columns(2)
    with col3:
        grade = st.selectbox(
            "Grade/Class *",
            ["Select", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", 
             "9th", "10th", "11th", "12th", "Undergraduate", "Graduate"]
        )
    with col4:
        course = st.text_input("Course/Major", placeholder="e.g., Computer Science")
    
    # Additional Information
    st.subheader("Additional Information")
    
    previous_school = st.text_input("Previous School/Institution")
    interests = st.multiselect(
        "Areas of Interest",
        ["Mathematics", "Science", "Literature", "Arts", "Sports", "Music", 
         "Technology", "Languages", "History", "Social Studies"]
    )
    
    # Terms and conditions
    terms = st.checkbox("I agree to the terms and conditions *")
    
    # Submit button
    submit_button = st.form_submit_button("Submit Registration")
    
    # Form validation and submission
    if submit_button:
        # Validation
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        if not email.strip():
            errors.append("Email is required")
        elif "@" not in email:
            errors.append("Please enter a valid email address")
        if gender == "Select":
            errors.append("Please select a gender")
        if grade == "Select":
            errors.append("Please select a grade/class")
        if not terms:
            errors.append("You must agree to the terms and conditions")
        
        # Display errors or success
        if errors:
            st.error("Please fix the following errors:")
            for error in errors:
                st.error(f"• {error}")
        else:
            # Process successful submission
            st.success("✅ Registration Successful!")
            
            # Display formatted information
            st.balloons()
            
            st.markdown("---")
            st.subheader("Registration Summary")
            
            st.write(f"**Name:** {name.title()}")
            st.write(f"**Email:** {email.lower()}")
            st.write(f"**Age:** {age}")
            st.write(f"**Gender:** {gender}")
            
            if phone:
                st.write(f"**Phone:** {phone}")
            if address:
                st.write(f"**Address:** {address}")
            
            st.write(f"**Grade/Class:** {grade}")
            if course:
                st.write(f"**Course/Major:** {course.title()}")
            if previous_school:
                st.write(f"**Previous School:** {previous_school.title()}")
            if interests:
                st.write(f"**Interests:** {', '.join(interests)}")
            

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>* Required fields</p>",
    unsafe_allow_html=True
)