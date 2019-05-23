async function ticket_count() {
    let value = await eel.ticket_count()();
    document.getElementById("count_tickets").innerHTML = value;
}

ticket_count();