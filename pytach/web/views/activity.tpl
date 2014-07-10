		<h2 class="content-subhead" id="{{activity["name"]}}">{{activity["description"]}}</h2>
		<p>
		% for command in activity["activities"]:
			% command_path = "{}/{}".format(activity["name"], command["name"])
			<button class="pure-button" onclick='post("{{ url('activity', activity=command_path) }}")'>{{command["description"] if "description" in command else command["name"]}}</button>
		% end
		</p>
		%rebase layout title=activity["description"], devices=devices, activities=activities