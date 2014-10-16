		<div class="pure-g">
		% for command in activity["activities"]:
			% command_path = "{}/{}".format(activity["name"], command["name"])
            <button class="pure-button pure-u-1-2 pure-u-md-1-3 pure-u-lg-1-4 {{command.get('css-class') or ''}}" onclick='post("{{ url('activity', activity=command_path) }}")'>
              % if command.get('icon'):
              <i class="fa {{ command.get('icon') }}"></i>
              % end
              {{command["description"] if "description" in command else command["name"]}}
            </button>
		% end
		</div>
		%rebase('layout.tpl', title=activity["description"], subtitle=activity.get('subtitle'), devices=devices, activities=activities)