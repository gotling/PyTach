<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{title or 'No title'}} | PyTach</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="{{ url('static', filename='images/icon300.png') }}">
    <link rel="apple-touch-icon-precomposed" href="{{ url('static', filename='images/icon152.png') }}">
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    <link rel="stylesheet" href="http://purecss.io/combo/1.15.4?/css/layouts/side-menu.css">
    <script src="{{ url('static', filename='microajax-mod.js') }}"></script>
    <style type="text/css">
    	h1 a {text-decoration: none; color: #333}
        .pure-button {
            margin-bottom: 1em;
            min-width: 5em;
        }
    </style>
</head>
<body>
<div id="layout">
    <a href="#menu" id="menuLink" class="menu-link">
        <span></span>
    </a>

    <div id="menu">
        <div class="pure-menu pure-menu-open">
            <a class="pure-menu-heading" href="#">Devices</a>
            <ul>
                % for device_name in devices:
                <li><a href="{{ url('device_view', device=device_name) }}">{{devices[device_name]["description"]}}</a></li>
                % end
            </ul>
            <a class="pure-menu-heading" href="#">Activities</a>
            <ul>
                % for activity_name in activities:
                <li><a href="{{ url('activity_view', activity=activity_name) }}">{{activities[activity_name]["description"]}}</a></li>
                % end
            </ul>
        </div>
    </div>

    <div id="main">
        <div class="header">
            <h1><a href="{{ url('main') }}">PyTach</a></h1>
            <h2>An interface to iTach</h2>
        </div>

        <div class="content">
            %include
        </div>
    </div>
</div>

<script src="http://purecss.io/combo/1.15.4?/js/ui.js"></script>
<script>
    function post(url) {
        microAjax(url, function(res) {
            console.log("POST: " + url + " Result: " + res);
        }, "{}");
    }
</script>
</body>
</html>
