function hash(str) {
            const crypto = window.crypto || window.msCrypto;
            const buffer = new TextEncoder("utf-8").encode(str);
            return crypto.subtle.digest("SHA-256", buffer).then(function (hash) {
                return hex(hash);
            });
        }

        function hex(buffer) {
            const hexCodes = [];
            const view = new DataView(buffer);
            for (var i = 0; i < view.byteLength; i += 4) {
                const value = view.getUint32(i)
                const stringValue = value.toString(16)
                const padding = '00000000'
                const paddedValue = (padding + stringValue).slice(-padding.length)
                hexCodes.push(paddedValue);
            }
            return hexCodes.join("");
        }

        function fetchIterations(username) {
            return $.ajax({
                url: "/get_iterations/",
                method: "GET",
                data: {username: username}
            });
        }

        function hashPassword(password, iterations) {
            return new Promise(function (resolve) {
                var hashedPassword = password;
                var count = 0;

                function hashNext() {
                    if (count < iterations - 1) {
                        hash(hashedPassword).then(function (result) {
                            hashedPassword = result;
                            count++;
                            hashNext();
                        });
                    } else {
                        resolve(hashedPassword);
                    }
                }

                hashNext();
            });
        }

function showSnackbar(message) {
    var snackbar = document.getElementById("snackbar");
    snackbar.innerHTML = message;
    snackbar.className = "show";
    setTimeout(function () {
        snackbar.className = snackbar.className.replace("show", "");
    }, 3000);
}

$(document).ready(function () {
    $("#login-form").submit(function (event) {
            event.preventDefault();
            const form = $(this);
            const username = form.find("input[name='username']").val();
            const password = form.find("input[name='password']").val();

            fetchIterations(username).then(function (data) {
                const iterations = data.iterations;
                alert('iteration: ' + iterations)
                if (iterations !== "Invalid request") {
                hashPassword(password, iterations).then(function (hashedPassword) {
                    $.ajax({
                        url: form.attr("action"),
                        method: form.attr("method"),
                        data: {
                            username: username,
                            password: hashedPassword,
                            iterations: iterations,
                            csrfmiddlewaretoken: form.find("input[name='csrfmiddlewaretoken']").val()
                        },
                        success: function (data) {
                            showSnackbar(data);
                        },
                        error: function (xhr, status, error) {
                            showSnackbar("An error occurred: " + error);
                        }
                    });
                });
                } else {
                    showSnackbar("User does not exist! Please register first.");
                }
            });
    });
});
