function addNote() {
    let text = document.getElementById('text').value
    let important = document.getElementById('important').checked
    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'text': text, 'important': important})
    }).then(() => location.reload())
}

function clearNotes() {
    fetch('/clear', {
        method: 'delete'

    }).then(() => location.reload())
}