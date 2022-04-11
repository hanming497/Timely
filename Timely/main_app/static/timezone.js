var app = {};

app.getAJAX = function () {

    let weatherUrl = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=ea43d349fe09f49a0d21b5607b77208c'

    fetch(weatherUrl)
        .then(data => {
            app.displayWeather(weatherCondition, weatherResponse);
            app.runClock(weatherResponse);
            // Handle data
        }).catch(error => {
            console.log('error')
            // Handle error
        });

}
//Displ
//Display Weather 

app.displayWeather = function (weatherCondition, weatherResponse) {

    var city = weatherResponse[0].name;
    var temperature = Math.round(weatherResponse[0].main.temp - 273.15);
    var tempFahrenheit = Math.round((weatherResponse[0].main.temp) * 9 / 5 - 459.67);
    var feelsLike = Math.round(weatherResponse[0].main.feels_like - 273.15);
    var currentCondition = weatherResponse[0].weather[0].main;

    document.querySelector('#city').text(city);

    document.querySelector('tempCheck').addEventListener('change', function () {
        if (this.checked) {
            //document.getElementById('#tempFahrenheit').fadeOut('slow', function () {
            // $('#temperature').fadeIn('slow');
            //});
        } else {
            // $('#temperature').fadeOut('slow', function () {
            // $('#tempFahrenheit').fadeIn('slow');
            // });
        }
    });

    if (temperature >= 29) {

        document.getElementsByClassName('.tile-weather').addClass('hot');
        document.getElementsByID('#temperature').text(temperature + '°C');
        document.getElementsByID('#tempFahrenheit').text(tempFahrenheit + '°F');

    } else if (temperature <= 5) {

        $('#temperature').text(temperature + '°C');
        $('#tempFahrenheit').text(tempFahrenheit + '°F');
        //$('#temperaturecondition').text('Brr! ');
        $('#hot').text("best to bring a winter jacket!");
        $('#weatherCommentary').addClass('is-hidden');

    } else {
        $('#temperature').text(temperature + '°C');
        $('#tempFahrenheit').text(tempFahrenheit + '°F');
    }

    //var lightWeather = weatherCondition.includes('Light');

    switch (currentCondition) {

        case 'Fog':
        case 'Clouds':

            $('.tile-weather').addClass('clouds');
            $('#weathercondition').text(currentCondition);
            $('#weatherCommentary').text(' an average, grey day in London.');

            break;

        case 'Haze':

            $('.tile-weather').addClass('haze');
            $('#weathercondition').text(currentCondition);
            $('#weatherCommentary').text(' an average day in London.');

            break;

        case 'Clear':

            $('.tile-weather').addClass('clear');
            $('#weathercondition').text(currentCondition);
            $('#weatherCommentary').text(' a good day in London.');

            //app.displayBadDay(weatherCondition);

            break;

        case 'Rain':
        case 'Light Rain':
        case 'Heavy Rain':


            $('.tile-weather').addClass('rain');
            $('#weathercondition').text(currentCondition + ' :(');
            $('#weatherStart').addClass('is-hidden');
            $('#weatherStart').addClass('is-hidden');
            $('#weatherCommentary').text(' best to bring an umbrella!');


            break;

        case 'Thunderstorm':

            $('.tile-weather').addClass('thunderstorm');
            $('#weathercondition').text(currentCondition + ' ⚡');
            $('#weatherStart').addClass('is-hidden');
            $('#weatherStart').addClass('is-hidden');
            $('#weatherCommentary').text(' best to stay indoors!');

            break;

        case 'Snow':

            $('.tile-weather').addClass('snow');
            $('#weathercondition').text(currentCondition);
            $('#weatherStart').addClass('is-hidden');
            $('#hot').append(' snowing in London?? Madness!');

            break;

        case 'Mist':
        case 'Drizzle':

            $('.tile-weather').addClass('mist');
            $('#weathercondition').text(currentCondition);
            $('#weatherStart').addClass('is-hidden');
            $('#weatherCommentary').text(' weather that is like your eyes watching Jack slip in ocean (spoiler!)');

            break;

        case 'Smoke':
        case 'Ash':
        case 'Squall':
        case 'Tornado':
        case 'Dust':
        case 'Sand':

            $('.tile-weather').addClass('hot');
            $('#weathercondition').text(currentCondition);
            $('#weatherStart').addClass('is-hidden');
            $('#weatherCommentary').text(' a pretty unusual day out there, stay safe mate!');

            break;

        default:
            $('#weathercondition').text(currentCondition);

    }

    if (feelsLike === temperature) {
        $('#feelslike').text('Feels similar');
    } else if (feelsLike <= temperature) {
        $('#feelslike').text('Feels cooler');
    } else if (feelsLike >= temperature) {
        $('#feelslike').text('Feels warmer');
        //$('#feelslike').text('Feels like ' + feelsLike + '°C');
        //else  if (Math.abs(temperature - feelsLike) <= 2) {
    }
};

app.runClock = function (weatherResponse) {

    londonTime = moment.tz.add('Europe/London|BST BDST GMT|0 -10 -20|0101010101010101010101010101010101010101010101010121212121210101210101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010|-2axa0 Rc0 1fA0 14M0 1fc0 1g00 1co0 1dc0 1co0 1oo0 1400 1dc0 19A0 1io0 1io0 WM0 1o00 14o0 1o00 17c0 1io0 17c0 1fA0 1a00 1lc0 17c0 1io0 17c0 1fA0 1a00 1io0 17c0 1io0 17c0 1fA0 1cM0 1io0 17c0 1fA0 1a00 1io0 17c0 1io0 17c0 1fA0 1a00 1io0 1qM0 Dc0 2Rz0 Dc0 1zc0 Oo0 1zc0 Rc0 1wo0 17c0 1iM0 FA0 xB0 1fA0 1a00 14o0 bb0 LA0 xB0 Rc0 1wo0 11A0 1o00 17c0 1fA0 1a00 1fA0 1cM0 1fA0 1a00 17c0 1fA0 1a00 1io0 17c0 1lc0 17c0 1fA0 1a00 1io0 17c0 1io0 17c0 1fA0 1a00 1a00 1qM0 WM0 1qM0 11A0 1o00 WM0 1qM0 WM0 1qM0 WM0 1qM0 WM0 1tA0 IM0 90o0 U00 1tA0 U00 1tA0 U00 1tA0 U00 1tA0 WM0 1qM0 WM0 1qM0 WM0 1tA0 U00 1tA0 U00 1tA0 11z0 1o00 11A0 1o00 11A0 1o00 11A0 1qM0 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1o00 14o0 1o00 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00 11A0 1qM0 WM0 1qM0 WM0 1qM0 WM0 1qM0 11A0 1o00 11A0 1o00');

    var hours = moment.tz('Europe/London').format('hh');
    var daylightSavings = moment.tz('Europe/London').isDST();

    var londonDate = moment.tz(londonTime).format('dddd, MMMM Do, YYYY');
    var londonEpoch = moment.tz(londonTime).format('X');

    var sunriseDataEpoch = weatherResponse[0].sys.sunrise;
    var sunsetDataEpoch = weatherResponse[0].sys.sunset;

    var sunriseDifferenceinSeconds = (sunriseDataEpoch - (+londonEpoch));
    //(sunriseDataEpoch - (+londonEpoch));
    var sunriseinHours = Math.round(sunriseDifferenceinSeconds / 3600);

    var sunsetDifferenceinSeconds = (sunsetDataEpoch - (+londonEpoch));
    var sunsetinHours = Math.round(sunsetDifferenceinSeconds / 3600);

    $('#day-label').text(londonDate);

    if (daylightSavings) {
        $('#currenttimezone').text('BST');
    } else {
        $('#currenttimezone').text(' GMT');
    }


    (function sunRise() {

        if (sunriseDifferenceinSeconds <= 29400 && sunriseDifferenceinSeconds > 3600 && sunriseinHours !== 1) {
            $('.tile-clock').addClass('nightime');
            $('#moon-svg').attr('src', 'img/moon.svg');
            $('#sunrise').removeClass('is-hidden');
            $('#sunset').addClass('is-hidden');
            $('#moon-svg').attr('src', 'img/moon.svg');
            $('#sunrise').text('Sunrise is in ' + sunriseinHours + ' hours ');

        } else if (sunriseinHours === 1) {
            $('.tile-clock').removeClass('nightime').addClass('sunset-after');
            $('#sunrise').removeClass('is-hidden');
            $('#sunset').addClass('is-hidden');
            $('#moon-svg').addClass('is-hidden');
            $('#sunrise').text('Sunrise is in an hour ');

        } else if (sunriseDifferenceinSeconds < 3600 && sunriseDifferenceinSeconds >= 500) {
            $('#sunrise').removeClass('is-hidden');
            $('#sunset').addClass('is-hidden');
            $('#moon-svg').addClass('is-hidden');
            $('.tile-clock').addClass('sunset-after');
            $('#sunrise').text('Sunrise is soon');

        } else if (sunriseDifferenceinSeconds < 500 && sunriseDifferenceinSeconds >= ~7200) {
            $('#sunrise').removeClass('is-hidden');
            $('#sunset').addClass('is-hidden');
            $('#moon-svg').addClass('is-hidden');
            $('.tile-clock').addClass('sunset');
            $('#sunrise').text('Dawn');

        } else if (sunriseDifferenceinSeconds < ~7200 && sunriseDifferenceinSeconds >= ~18000 && sunriseinHours !== -1) {
            $('#sunset').addClass('is-hidden');
            $('#moon-svg').addClass('is-hidden');
            $('.tile-clock').removeClass('sunset');
            $('#sunrise').text('Sunrise was ' + (sunriseinHours * -1) + ' hours ago ');

        } else if (sunriseDifferenceinSeconds < ~18000 && sunriseDifferenceinSeconds >= ~21600) {
            $('#sunrise').text('Midday');
            $('#moon-svg').addClass('is-hidden');
            $('.tile-clock').removeClass('sunset');
        }

        setTimeout(sunRise, 1000);

    })();

    (function sunSet() {

        if (sunsetDifferenceinSeconds <= 10800 && sunsetDifferenceinSeconds > 3600) {
            $('#sunrise').addClass('is-hidden');
            $('#sunset').text('Sunset is in ' + sunsetinHours + ' hours ');
            $('#moon-svg').addClass('is-hidden');

        } else if (sunsetDifferenceinSeconds === 3600) {
            $('.tile-clock').addClass('sunset-before');
            $('#moon-svg').addClass('is-hidden');
            $('#sunset').text('Sunset is in an hour ');

        } else if (sunsetDifferenceinSeconds < 3600 && sunsetDifferenceinSeconds >= 500) {
            $('#sunrise').addClass('is-hidden');
            $('.tile-clock').removeClass('sunset').addClass('sunset-before');
            $('#moon-svg').addClass('is-hidden');
            $('#sunset').text('Sunset is soon');

        } else if (sunsetDifferenceinSeconds < 500 && sunsetDifferenceinSeconds >= ~3600) {
            $('#sunrise').addClass('is-hidden');
            $('.tile-clock').removeClass('sunset-before').addClass('sunset');
            $('#moon-svg').addClass('is-hidden');
            $('#sunset').text('Sunset');

        } else if (sunsetDifferenceinSeconds < ~3600 && sunsetDifferenceinSeconds > ~7200) {
            $('.tile-clock').removeClass('sunset').addClass('sunset-after');
            $('#sunrise').text('Sunset was an hour ago ');
            $('#moon-svg').addClass('is-hidden');
        }

        else if (sunsetDifferenceinSeconds <= ~7200 && sunsetDifferenceinSeconds >= ~10800) {
            $('.tile-clock').removeClass('sunset-after').addClass('nightime');
            $('#sunrise').text('Sunset was ' + (sunsetinHours * -1) + ' hours ago ');
            $('#moon-svg').attr('src', 'img/moon.svg');

        }

        else if (sunsetDifferenceinSeconds < ~10800 && sunsetDifferenceinSeconds > ~29400) {
            $('.tile-clock').addClass('nightime');
            $('#sunrise').addClass('is-hidden');
            $('#sunset').text('Nightime ');
            $('#moon-svg').attr('src', 'img/moon.svg');

        }

        setTimeout(sunSet, 1000);

    })();

    var dialLines = $('.diallines');

    for (var i = 1; i <= 60; i++) {
        dialLines[i] = $(dialLines[i - 1]).clone().insertAfter($(dialLines[i - 1]));
        $(dialLines[i]).css('transform', 'rotate(' + 6 * i + 'deg)');
    }

    function tick() {

        var seconds = moment.tz(londonTime).format('ss');
        var minutes = moment.tz(londonTime).format('mm');
        var hours = moment.tz('Europe/London').format('hh');

        var secAngle = seconds * 6;
        var minAngle = minutes * 6 + seconds * (360 / 3600);
        var hourAngle = hours * 30 + minutes * (360 / 720);

        if (secAngle === 0) {
            $('.sec-hand').removeClass('hand-movement');
        } else {
            $('.sec-hand').addClass('hand-movement');
        }
        if (minAngle === 0) {
            $('.min-hand').removeClass('hand-movement');
        } else {
            $('.min-hand').addClass('hand-movement');
        }
        $('.sec-hand').css('transform', 'rotate(' + secAngle + 'deg)');
        $('.min-hand').css('transform', 'rotate(' + minAngle + 'deg)');
        $('.hour-hand').css('transform', 'rotate(' + hourAngle + 'deg)');

    }

    setInterval(tick, 100);

};

app.loaderFadeOut = function () {

    var twentyFourHours = moment.tz('Europe/London').format('HH');
    var timedifference = new Date().getTimezoneOffset();

    var userTime = new Date().getHours();

    (function loaderGreeting() {

        if (userTime >= 1 && userTime < 5) {
            $('.loader-greeting').text('Hello night owl');

        } else if (userTime >= 5 && userTime < 12) {
            $('.loader-greeting').text('Morning');

        } else if (userTime >= 12 && userTime < 17) {
            $('.loader-greeting').text('Afternoon');

        } else if (userTime >= 17 || userTime < 1) {
            $('.loader-greeting').text('Good evening');

        }
        setTimeout(loaderGreeting, 5000);

    })();

    setTimeout(function () {
        $('.loading-text').removeClass("fadeInUp");
        $('.loading-text').addClass("fadeOutUp");
        $('#loader-1').removeClass("fadeInUp");
        $('#loader-1').addClass("fadeOutUp");
        $('.loading-header').addClass("animated animatedFadeInUp fadeOutUp");
    }.bind(this), 1000);

};

app.removeWidget = function () {

    $('#closeMessage').on('click', function (c) {
        $(this).closest('.tile-message').fadeOut('slow');
    });
};

app.init = function () {
    app.loaderFadeOut();
    app.getAJAX();
    app.removeWidget();
};

$(document).ready(app.init);
