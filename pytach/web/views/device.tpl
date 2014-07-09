<h2 class="content-subhead" id="{{device["name"]}}">{{device["description"]}}</h2>
<p>
% for command in device["commands"]:
	% command_path = "{}/{}".format(device["name"], command["name"])
	<button class="pure-button" onclick='post("{{ url('device', device=command_path) }}")'>{{command["description"] if "description" in command else command["name"]}}</button>
% end
</p>
%rebase layout title=device["description"]