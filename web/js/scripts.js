async function ticket_count() {
    let value = await eel.ticket_count()();
    document.getElementsByClassName("counter"). innerHTML = value;
}