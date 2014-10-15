		<h2 class="content-subhead" id="{{activity["name"]}}">{{activity["description"]}}</h2>
		<div class="pure-g">
		% for command in activity["activities"]:
			% command_path = "{}/{}".format(activity["name"], command["name"])
            <button class="pure-button pure-u-1-2 pure-u-md-1-3 pure-u-lg-1-4 {{command.get('css-class') or ''}}" onclick='post("{{ url('activity', activity=command_path) }}")'>{{command["description"] if "description" in command else command["name"]}}</button>
		% end
		</div>
		%rebase('layout.tpl', title=activity["description"], devices=devices, activities=activities)