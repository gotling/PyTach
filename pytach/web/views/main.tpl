		<h2 class="content-subhead" id="introduction">Introduction</h2>
		<p>
			Use the menu on the left to access your devices and activities.
		</p>

		<h2 class="content-subhead" id="configuration">Configuration</h2>
		<p>
			Devices and activities are stored as <a href="http://json.org" target="_blank">JSON</a> files in their own folders in PyTachs installation folder. Create or update configuration files and pass them throgh <a href="http://pro.jsonlint.com/" target="_blank">JSON Lint</a> to make sure their valid JSON files. Then restart PyTach to have them appear here.
		</p>

		<h2 class="content-subhead" id="project">Project</h2>
		<p>
			The project is hosted on <a href="https://github.com/gotling/PyTach" target="_blank">GitHub</a> where you can get updates and submit bugs.
		</p>

		%rebase('layout.tpl', title="PyTach", devices=devices, activities=activities)