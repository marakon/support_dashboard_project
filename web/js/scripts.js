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

eel.expose(unassignedTransfer);
function unassignedTransfer(count) {
    document.getElementById("count_transfer").innerHTML = count;
}

eel.expose(pickupRate);
function pickupRate(count) {
    document.getElementById("mat_pickup").innerHTML = count[0];
    document.getElementById("bart_pickup").innerHTML = count[1];
    document.getElementById("harsh_pickup").innerHTML = count[2];
    document.getElementById("woj_pickup").innerHTML = count[3];
    document.getElementById("jak_pickup").innerHTML = count[4];
}

eel.expose(unassignedList);
function unassignedList(list) {
    var ticketList = list;

    var getTable = document.getElementById('ticket-table-list');

    while(getTable.hasChildNodes()) {
        getTable.removeChild(getTable.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        if (i === 7) {
            break;
        }

        var trElement = document.createElement('tr');

        document.getElementById('ticket-table-list').appendChild(trElement);

        for(var n = 0; n < ticketList[i].length; n++){
            var tdItem = document.createElement('td');

            tdItem.innerHTML = ticketList[i][n];

            trElement.appendChild(tdItem);
        }
    }
}

eel.expose(notAnsweredList);
function notAnsweredList(list) {
    var ticketList = list;

    var getTable = document.getElementById('na-ticket-table-list');

    while(getTable.hasChildNodes()) {
        getTable.removeChild(getTable.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        if (i === 12) {
            break;
        }

        var trElement = document.createElement('tr');

        document.getElementById('na-ticket-table-list').appendChild(trElement);

        for(var n = 0; n < ticketList[i].length; n++){
            var tdItem = document.createElement('td');
            tdItem.className = "td-na";

            tdItem.innerHTML = ticketList[i][n];

            trElement.appendChild(tdItem);
        }
    }
}

