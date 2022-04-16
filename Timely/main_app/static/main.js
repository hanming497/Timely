var app = {};



app.sunRise = function () {

    if (sunriseDifferenceinSeconds <= 29400 && sunriseDifferenceinSeconds > 3600 && sunriseinHours !== 1) {
        $('.tile-weather').addClass('nightime');
        //$('#moon-svg').attr('src', 'img/moon.svg');
        $('#sunrise').text('Sunrise is in ' + sunriseinHours + ' hours ');

    } else if (sunriseinHours === 1) {
        $('.tile-weather').removeClass('nightime').addClass('sunset-after');
        //$('#moon-svg').addClass('is-hidden');

    } else if (sunriseDifferenceinSeconds < 3600 && sunriseDifferenceinSeconds >= 500) {
        //$('#moon-svg').addClass('is-hidden');
        $('.tile-weather').addClass('sunset-after');

    } else if (sunriseDifferenceinSeconds < 500 && sunriseDifferenceinSeconds >= ~7200) {
        //$('#moon-svg').addClass('is-hidden');
        $('.tile-weather').addClass('sunset');

    } else if (sunriseDifferenceinSeconds < ~7200 && sunriseDifferenceinSeconds >= ~18000 && sunriseinHours !== -1) {
        //$('#moon-svg').addClass('is-hidden');
        $('.tile-weather').removeClass('sunset');

    } else if (sunriseDifferenceinSeconds < ~18000 && sunriseDifferenceinSeconds >= ~21600) {
        //$('#sunrise').text('Midday');
        $('.tile-weather').removeClass('sunset');
    }

    setTimeout(sunRise, 1000);
}

app.sunSet = function () {

    if (sunsetDifferenceinSeconds <= 10800 && sunsetDifferenceinSeconds > 3600) {
        //$('#moon-svg').addClass('is-hidden');

    } else if (sunsetDifferenceinSeconds === 3600) {
        $('.tile-weather').addClass('sunset-before');
        //$('#moon-svg').addClass('is-hidden');

    } else if (sunsetDifferenceinSeconds < 3600 && sunsetDifferenceinSeconds >= 500) {
        $('.tile-weather').removeClass('sunset').addClass('sunset-before');

    } else if (sunsetDifferenceinSeconds < 500 && sunsetDifferenceinSeconds >= ~3600) {
        $('.tile-weather').removeClass('sunset-before').addClass('sunset');
        //$('#moon-svg').addClass('is-hidden');

    } else if (sunsetDifferenceinSeconds < ~3600 && sunsetDifferenceinSeconds > ~7200) {
        $('.tile-weather').removeClass('sunset').addClass('sunset-after');
        //$('#moon-svg').addClass('is-hidden');
    }

    else if (sunsetDifferenceinSeconds <= ~7200 && sunsetDifferenceinSeconds >= ~10800) {
        $('.tile-weather').removeClass('sunset-after').addClass('nightime');
        //$('#moon-svg').attr('src', 'img/moon.svg');

    }

    else if (sunsetDifferenceinSeconds < ~10800 && sunsetDifferenceinSeconds > ~29400) {
        $('.tile-weather').addClass('nightime');
        //$('#moon-svg').attr('src', 'img/moon.svg');

    }

    setTimeout(sunSet, 1000);

}

app.removeWidget = function () {

    $('#closeMessage').on('click', function (c) {
        $(this).closest('.tile-message').fadeOut('slow');
    });
};


app.init = function () {
    app.removeWidget();
};

$(document).ready(app.init);
