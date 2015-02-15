/* A short script to prevent internal links to a "webapp" added to iPhone home screen to open in Safari
 instead of navigating internally.

https://gist.github.com/irae/1042167 */
(function(document,navigator,standalone) {
    if ((standalone in navigator) && navigator[standalone]) {
        var curnode, location=document.location, stop=/^(a|html)$/i;
        document.addEventListener('click', function(e) {
            curnode=e.target;
            while (!(stop).test(curnode.nodeName)) {
                curnode=curnode.parentNode;
            }
            if (
                'href' in curnode && // is a link
                (chref=curnode.href).replace(location.href,'').indexOf('#') &&
                (	!(/^[a-z\+\.\-]+:/i).test(chref) ||
                    chref.indexOf(location.protocol+'//'+location.host)===0 )
            ) {
                e.preventDefault();
                location.href = curnode.href;
            }
        },false);
    }
})(document,window.navigator,'standalone');