<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{title or 'No title'}} | PyTach</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="mobile-web-app-capable" content="yes">
    <link rel="apple-touch-icon" sizes="57x57" href="{{ url('static', filename='images/favicon/apple-touch-icon-57x57.png') }}">
    <link rel="apple-touch-icon" sizes="60x60" href="{{ url('static', filename='images/favicon/apple-touch-icon-60x60.png') }}">
    <link rel="apple-touch-icon" sizes="72x72" href="{{ url('static', filename='images/favicon/apple-touch-icon-72x72.png') }}">
    <link rel="apple-touch-icon" sizes="76x76" href="{{ url('static', filename='images/favicon/apple-touch-icon-76x76.png') }}">
    <link rel="apple-touch-icon" sizes="114x114" href="{{ url('static', filename='images/favicon/apple-touch-icon-114x114.png') }}">
    <link rel="apple-touch-icon" sizes="120x120" href="{{ url('static', filename='images/favicon/apple-touch-icon-120x120.png') }}">
    <link rel="apple-touch-icon" sizes="144x144" href="{{ url('static', filename='images/favicon/apple-touch-icon-144x144.png') }}">
    <link rel="apple-touch-icon" sizes="152x152" href="{{ url('static', filename='images/favicon/apple-touch-icon-152x152.png') }}">
    <link rel="apple-touch-icon" sizes="180x180" href="{{ url('static', filename='images/favicon/apple-touch-icon-180x180.png') }}">
    <link rel="icon" type="image/png" href="{{ url('static', filename='images/favicon/favicon-32x32.png') }}" sizes="32x32">
    <link rel="icon" type="image/png" href="{{ url('static', filename='images/favicon/android-chrome-192x192.png') }}" sizes="192x192">
    <link rel="icon" type="image/png" href="{{ url('static', filename='images/favicon/favicon-96x96.png') }}" sizes="96x96">
    <link rel="icon" type="image/png" href="{{ url('static', filename='images/favicon/favicon-16x16.png') }}" sizes="16x16">
    <link rel="manifest" href="{{ url('static', filename='images/favicon/android-chrome-manifest.json') }}">
    <meta name="msapplication-TileColor" content="#0c0c0c">
    <meta name="msapplication-TileImage" content="/mstile-144x144.png">
    <meta name="theme-color" content="#ffffff">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/grids-responsive-min.css">
    <link rel="stylesheet" href="https://pure-css.github.io/layouts/side-menu/styles.css">
    <link rel="stylesheet" href="{{ url('static', filename='pytach.css') }}">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
    <script src="{{ url('static', filename='stay-standalone.js') }}"></script>
    <script src="{{ url('static', filename='microajax-mod.js') }}"></script>
    <script src="{{ url('static', filename='hammer.min.js') }}"></script>
</head>
<body class="dark">
<div id="layout">
    <a href="#menu" id="menuLink" class="menu-link">
        <span></span>
    </a>

    <div id="menu">
        <div class="pure-menu pure-menu-open">
            <a class="pure-menu-heading" href="#">Activities</a>
            <ul class="pure-menu-list">
                % for activity_name in activities:
                <li class="pure-menu-item"><a href="{{ url('activity_view', activity=activity_name) }}" class="pure-menu-link">{{activities[activity_name]["description"]}}</a></li>
                % end
            </ul>
            <a class="pure-menu-heading" href="#">Devices</a>
            <ul class="pure-menu-list">
                % for device_name in devices:
                <li class="pure-menu-item"><a href="{{ url('device_view', device=device_name) }}" class="pure-menu-link">{{devices[device_name]["description"]}}</a></li>
                % end
            </ul>
        </div>
    </div>

    <div id="main">
        <div class="header">
            <h1><a href="{{ url('main') }}">{{title or 'PyTach'}}</a></h1>
            % if defined('subtitle') and subtitle:
            <h2>{{ subtitle }}</h2>
            % end
            <span id="debug"></span>
        </div>

        <div class="content">
            {{!base}}
        </div>
    </div>
</div>

<script src="https://pure-css.github.io/js/ui.js"></script>
<script>
    function post(url) {
        microAjax(url, function(res) {
            console.log("POST: " + url + " Result: " + res);
        }, "{}");
    }

    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };

    window.scrollTo(0,1);

    var main = document.getElementById('main');
    var debug = document.getElementById('debug');
    var mc = new Hammer(main);

    <%
    pages = [url('activity_view', activity=activity_name) for activity_name in activities]
    pages.extend([url('device_view', device=device_name) for device_name in devices])
    %>
    var pages = {{ !pages }};
    var page_index = 0;
    for (var index in pages) {
        if (pages[index].endsWith("{{ request.path }}")) {
            page_index = index;
        }
    }

    mc.on("swipeleft swiperight", function(ev) {
        if (ev.type == "swipeleft") {
            if (page_index < pages.length -1) {
                page_index++;
                window.location.href = pages[page_index];
            }
        } else if (ev.type == "swiperight") {
            if (page_index > 0) {
                page_index--;
                window.location.href = pages[page_index];
            }
        }
    });
</script>
</body>
</html>
