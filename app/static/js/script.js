
// ======================================
// DELETE CONFIRMATION
// ======================================

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this record?"
    );

}


// ======================================
// EMPLOYEE SEARCH
// ======================================

function searchEmployees() {

    let input = document.getElementById("employeeSearch");

    if (!input) {
        return;
    }

    let searchValue = input.value.toLowerCase();

    let rows = document.querySelectorAll(
        "#employeeTable tbody tr"
    );

    rows.forEach(function(row) {

        let rowText = row.innerText.toLowerCase();

        if (rowText.includes(searchValue)) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}


// ======================================
// COURSE SEARCH
// ======================================

function searchCourses() {

    let input = document.getElementById("courseSearch");

    if (!input) {
        return;
    }

    let searchValue = input.value.toLowerCase();

    let courses = document.querySelectorAll(".course-card");

    courses.forEach(function(course) {

        let courseText = course.innerText.toLowerCase();

        if (courseText.includes(searchValue)) {

            course.style.display = "";

        } else {

            course.style.display = "none";

        }

    });

}


// ======================================
// PASSWORD SHOW / HIDE
// ======================================

function togglePassword() {

    let passwordInput = document.getElementById("password");

    if (!passwordInput) {
        return;
    }

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

    } else {

        passwordInput.type = "password";

    }

}


// ======================================
// FORM VALIDATION
// ======================================

function validateForm() {

    let inputs = document.querySelectorAll(
        "input[required], select[required]"
    );

    for (let input of inputs) {

        if (input.value.trim() === "") {

            alert("Please fill all required fields.");

            input.focus();

            return false;

        }

    }

    return true;

}


// ======================================
// ENROLLMENT CONFIRMATION
// ======================================

function confirmEnrollment() {

    return confirm(
        "Do you want to enroll in this course?"
    );

}


// ======================================
// SKILL GAP DISPLAY
// ======================================

function calculateSkillGap() {

    let currentLevel = Number(
        document.getElementById("currentLevel").value
    );

    let requiredLevel = Number(
        document.getElementById("requiredLevel").value
    );

    let gap = requiredLevel - currentLevel;

    if (gap < 0) {

        gap = 0;

    }

    let result = document.getElementById("gapResult");

    if (result) {

        result.innerText = "Skill Gap: " + gap;

    }

}


// ======================================
// PAGE LOAD
// ======================================

document.addEventListener("DOMContentLoaded", function() {

    console.log(
        "Employee Learning Recommendation System loaded successfully."
    );

});
