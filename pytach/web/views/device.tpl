		<div class="pure-g">
		% for command in device["commands"]:
			% command_path = "{}/{}".format(device["name"], command["name"])
			<div class="pure-u-1-3 pure-u-md-1-3 pure-u-lg-1-4">
                <button class="pure-button {{command.get('css-class') or ''}}" onclick='post("{{ url('device', device=command_path) }}")'>
                  % if command.get('icon'):
                  <i class="fa {{ command.get('icon') }}"></i>
                  % end
                  {{command["description"] if "description" in command else command["name"]}}
                </button>
            </div>
		% end
		</div>
		%rebase('layout.tpl', title=device["description"], subtitle=device.get('subtitle'), devices=devices, activities=activities)