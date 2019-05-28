var myVar = setInterval(ticket_count, 5000);

async function ticket_count() {
    var value = await eel.test_request()();
}

eel.expose(unassignedCount);
function unassignedCount(count) {
    document.getElementById("count_tickets").innerHTML = count;
}

eel.expose(unassignedPlatinum);
function unassignedPlatinum(count) {
    document.getElementById("count_platinum").innerHTML = count;
}

eel.expose(unassignedPremium);
function unassignedPremium(count) {
    document.getElementById("count_premium").innerHTML = count;
}