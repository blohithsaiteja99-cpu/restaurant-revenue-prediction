// =====================================================
// RESTAURANT REVENUE AI
// FRONTEND JAVASCRIPT
// =====================================================


// =====================================================
// ELEMENTS
// =====================================================

const form = document.getElementById("predictionForm");

const predictButton =
    document.getElementById("predictButton");

const resetButton =
    document.getElementById("resetButton");

const themeToggle =
    document.getElementById("themeToggle");


// =====================================================
// FORM SUBMISSION
// =====================================================

if (form && predictButton) {

    form.addEventListener(
        "submit",
        function () {

            predictButton.disabled = true;

            predictButton.innerHTML =
                "⏳ Predicting Revenue...";

        }
    );

}


// =====================================================
// RESET
// =====================================================

if (resetButton) {

    resetButton.addEventListener(
        "click",
        function () {

            setTimeout(
                function () {

                    window.location.href = "/";

                },
                100
            );

        }
    );

}


// =====================================================
// DARK MODE
// =====================================================

if (themeToggle) {

    themeToggle.addEventListener(
        "click",
        function () {

            document.body.classList.toggle(
                "dark-mode"
            );


            if (
                document.body.classList.contains(
                    "dark-mode"
                )
            ) {

                themeToggle.innerHTML = "☀️";

            }

            else {

                themeToggle.innerHTML = "🌙";

            }

        }
    );

}


// =====================================================
// SCROLL TO FORM
// =====================================================

function scrollToForm() {

    const inputPanel =
        document.querySelector(".input-panel");

    if (inputPanel) {

        inputPanel.scrollIntoView({

            behavior: "smooth",

            block: "start"

        });

    }

}


// =====================================================
// NUMBER VALIDATION
// =====================================================

const numberInputs =
    document.querySelectorAll(
        'input[type="number"]'
    );


numberInputs.forEach(
    function (input) {

        input.addEventListener(
            "input",
            function () {

                if (
                    this.value < 0 &&
                    this.name !== "Restaurant_Age"
                ) {

                    this.value = 0;

                }

            }
        );

    }
);