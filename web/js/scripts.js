var myVar = setInterval(ticket_count, 5000);

async function ticket_count() {
    var value = await eel.test_request()();
    document.getElementById("count_tickets").innerHTML = value;
}
