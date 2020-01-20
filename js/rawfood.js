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
        return today(timestamp) + 'T00:01:00';
    }

    var begin_day_timestamp = function(timestamp) {
        var nb_seconds = 86400;
        return Math.floor(timestamp / nb_seconds) * nb_seconds;
    }

    var end_day = function(timestamp) {
        return today(timestamp) + 'T23:59:00';
    }

    var end_day_timestamp = function(timestamp) {
        var nb_seconds = 86400;
        return begin_day_timestamp(timestamp) + nb_seconds;
    }

    return {
        'today': today,
        'get_timestamp': get_timestamp,
        'begin_day_timestamp': begin_day_timestamp,
        'end_day_timestamp': end_day_timestamp
    }
})();