cat > static/mywebscript.js <<'EOF'
let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseDiv = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        responseDiv.innerHTML = "Please enter some text.";
        return;
    }

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200) {
                responseDiv.innerHTML = this.responseText;
            } else {
                responseDiv.innerHTML = "Unable to analyze text.";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
};
EOF