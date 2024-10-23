function resetForm() {
    document.getElementById('codeForm').reset();
    document.getElementById('codearea').value = '';
    document.getElementById('output').value = '';
}

function retunfunction() {
    window.location.href = '/compiler/';
}

function cleanCodeArea(event) {
    event.preventDefault();
    let codeArea = document.getElementById("codearea");
    let codeLines = codeArea.value.split("\n");
    codeLines[0] = codeLines[0].replace(/^\s+/, '');
    codeArea.value = codeLines.join("\n");
    document.getElementById("codeForm").submit();
}