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

eel.expose(closureRate)
function closureRate(count) {
    document.getElementById("mat_closure").innerHTML = count[0];
    document.getElementById("bart_closure").innerHTML = count[1];
    document.getElementById("harsh_closure").innerHTML = count[2];
    document.getElementById("woj_closure").innerHTML = count[3];
    document.getElementById("jak_closure").innerHTML = count[4];
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

//////////////////////////////////////////////////////////////
// Clock 

function dateToText(date) {
    var hours = date.getHours()
    var minutes = date.getMinutes();
    // var seconds = date.getSeconds();
    if (minutes < 10) minutes = '0'+minutes;
    //if  seconds < 10) seconds = '0'+seconds;
    if (hours < 10) hours = '0'+hours;
    return hours + ":" + minutes; // + ":" + seconds;
}
function updateClocks() {
	for (var i = 0; i < window.arrClocks.length; i++) {
		var clock = window.arrClocks[i];
		var offset = window.arrOffsets[i];
		clock.innerHTML = dateToText(new Date(new Date().getTime()+offset));
	}
}
function startClocks() {
	clockElements = document.getElementsByClassName('clock');
	window.arrClocks = []
	window.arrOffsets = [];
	var j = 0;
	for(var i = 0; i < clockElements.length; i++) {
		el = clockElements[i];
		timezone = parseInt(el.getAttribute('timezone'));
		if (!isNaN(timezone)) {
			var tzDifference = timezone * 60 + (new Date()).getTimezoneOffset();
			var offset = tzDifference * 60 * 1000;
			window.arrClocks.push(el);
			window.arrOffsets.push(offset);
		}
	}
	updateClocks();
	clockID = setInterval(updateClocks, 1000);
}
setTimeout(startClocks, 100);