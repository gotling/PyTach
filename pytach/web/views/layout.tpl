<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{title or 'No title'}} | PyTach</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="static/images/icon300.png">
    <link rel="apple-touch-icon-precomposed" href="static/images/icon152.png">
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    <link rel="stylesheet" href="http://purecss.io/combo/1.15.4?/css/layouts/side-menu.css">
    <script src="{{ url('static', filename='microajax-mod.js') }}"></script>
</head>
<body>
<div id="layout">
    <a href="#menu" id="menuLink" class="menu-link">
        <span></span>
    </a>

    <div id="menu">
        <div class="pure-menu pure-menu-open">
            <a class="pure-menu-heading" href="#">Menu</a>

            <ul>
                <li><a href="#">{{title or 'Unknown'}}</a></li>
            </ul>
        </div>
    </div>

    <div id="main">
        <div class="header">
            <h1>PyTach</h1>
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
