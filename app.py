import streamlit as st

def main():
    st.title("Prelim Grade Calculator")
    st.write("Enter your grades to calculate your prelim grade and see what you need for the remaining terms.")
    
    # Create a form for user input
    with st.form("grade_form"):
        st.header("Input Grades")
        
        col1, col2 = st.columns(2)
        
        with col1:
            absences = st.number_input(
                "Number of Absences", 
                min_value=0, 
                max_value=10, 
                value=0,
                help="Enter the number of classes you've missed"
            )
            
            prelim_exam_grade = st.number_input(
                "Prelim Exam Grade (0-100)", 
                min_value=0.0, 
                max_value=100.0, 
                value=0.0,
                step=0.1,
                help="Enter your prelim exam score"
            )
            
        with col2:
            quizzes_grade = st.number_input(
                "Quizzes Grade (0-100)", 
                min_value=0.0, 
                max_value=100.0, 
                value=0.0,
                step=0.1,
                help="Enter your average quiz score"
            )
            
            requirements_grade = st.number_input(
                "Requirements Grade (0-100)", 
                min_value=0.0, 
                max_value=100.0, 
                value=0.0,
                step=0.1,
                help="Enter your requirements/assignments score"
            )
        
        recitation_grade = st.number_input(
            "Recitation Grade (0-100)", 
            min_value=0.0, 
            max_value=100.0, 
            value=0.0,
            step=0.1,
            help="Enter your recitation/participation score"
        )
        
        calculate_button = st.form_submit_button("Calculate Grades")
    
    if calculate_button:
        # Check for absences first
        if absences >= 4:
            st.error("❌ FAILED due to absences. You have 4 or more absences.")
            return
        
        # Calculate grades
        attendance_grade = 100 - (10 * absences)
        class_standing = (0.4 * quizzes_grade) + (0.3 * requirements_grade) + (0.3 * recitation_grade)
        prelim_grade = (0.6 * prelim_exam_grade) + (0.1 * attendance_grade) + (0.3 * class_standing)
        
        # Display results
        st.success("✅ Grade Calculation Complete!")
        
        st.subheader("Results")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Attendance Grade", f"{attendance_grade:.2f}")
            st.metric("Class Standing", f"{class_standing:.2f}")
        
        with col2:
            st.metric("Prelim Grade", f"{prelim_grade:.2f}", 
                     delta="Passing" if prelim_grade >= 75 else "Needs Improvement")
        
        st.divider()
        
        # Required grades calculations
        st.subheader("Required Grades for Future Terms")
        
        required_midterm_pass = max(0, (75 - (0.2 * prelim_grade)) / 0.3)
        required_final_pass = max(0, (75 - (0.2 * prelim_grade)) / 0.5)
        
        required_midterm_dean = max(0, (90 - (0.2 * prelim_grade)) / 0.3)
        required_final_dean = max(0, (90 - (0.2 * prelim_grade)) / 0.5)
        
        st.write("**To PASS the course (75% overall):**")
        st.write(f"- Required Midterm Grade: {required_midterm_pass:.2f}")
        st.write(f"- Required Final Grade: {required_final_pass:.2f}")
        
        st.write("**To become DEAN'S LISTER (90% overall):**")
        st.write(f"- Required Midterm Grade: {required_midterm_dean:.2f}")
        st.write(f"- Required Final Grade: {required_final_dean:.2f}")
        
        # Additional feedback
        st.divider()
        st.subheader("Performance Analysis")
        
        if prelim_grade >= 90:
            st.success("🎉 Excellent performance! You're on track for Dean's Lister!")
        elif prelim_grade >= 75:
            st.info("👍 Good job! You're passing and have room for improvement.")
        else:
            st.warning("⚠️ You need to improve your performance to pass the course.")

if __name__ == "__main__":
    main()
