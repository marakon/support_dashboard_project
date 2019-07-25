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

eel.expose(unassignedList);
function unassignedList(list) {
    var ticketList = list;

    var getDiv = document.getElementById('queueList');

    while(getDiv.hasChildNodes()) {
        getDiv.removeChild(getDiv.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        var objToArr = Object.values(ticketList[i]);

        var listElement = document.createElement('ul');

        document.getElementById('queueList').appendChild(listElement);

        for(var n = 0; n < objToArr.length; n++){
            var listItem = document.createElement('li');

            listItem.innerHTML = objToArr[n];

            listElement.appendChild(listItem);
        }

    }
}

eel.expose(notAnsweredList);
function notAnsweredList(list) {
    var ticketList = list;

    var getDiv = document.getElementById('naList');

    while(getDiv.hasChildNodes()) {
        getDiv.removeChild(getDiv.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        var objToArr = Object.values(ticketList[i]);

        var listElement = document.createElement('ul');

        document.getElementById('queueList').appendChild(listElement);

        for(var n = 0; n < objToArr.length; n++){
            var listItem = document.createElement('li');

            listItem.innerHTML = objToArr[n];

            listElement.appendChild(listItem);
        }

    }
}