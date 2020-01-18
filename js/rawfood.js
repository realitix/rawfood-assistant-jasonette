var rawfood = (function () {
    var get_timestamp = function() {
        return Date.now()/1000;
    }

    // Prefix number for always two zero
    var pn = function(n) {
        return ('0' + n).slice(-2)
    }

    var today = function(timestamp) {
        // Returned format yyyy-MM-dd'T'HH:mm
        var date = new Date(parseInt(timestamp)*1000);
        var y = date.getFullYear();
        // 0-11 becomes 1-12
        var m = date.getMonth() + 1; 
        var d = date.getDate();
        return y + '-' + pn(m) + '-' + pn(d);
    }

    var begin_day = function(timestamp) {
        return today(timestamp) + 'T00:01';
    }

    var end_day = function(timestamp) {
        return today(timestamp) + 'T23:59';
    }

    return {
        'get_timestamp': get_timestamp,
        'begin_day': begin_day,
        'end_day': end_day,
        'today': today
    }
})();