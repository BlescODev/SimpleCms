app.directive('scmsLinksEdit', function($compile) {
	return {
		restrict: 'E',
		scope: {
			links: "="
		},
		templateUrl: "/html/directives/scms-links-edit.tpl.html",

		link: function(scope) {
			scope.link = {
				url: "",
				text: ""
			};

			scope.editLink = function(index) {
				var linkEdit = document.getElementById("link-edit-" + index);
				linkEdit.style.display = "initial";
			}

			scope.updateLink = function(index) {
				var linkEdit = document.getElementById("link-edit-" + index);
				linkEdit.style.display = "none";
			}

			scope.addLink = function() {
				var linkEdit = document.getElementById("link-edit");
				linkEdit.style.display = "initial";
			};

			scope.cancelLink = function() {				
				var linkEdit = document.getElementById("link-edit");
				linkEdit.style.display = "none";

				scope.link = {
					type: "",
					source: ""
				};
			};

			scope.saveLink = function() {
				var size = Object.keys(scope.links).length;
				scope.links[size + 1] = scope.link;

				var linkEdit = document.getElementById("link-edit");
				linkEdit.style.display = "none";

				scope.link = {
					type: "",
					source: ""
				};
			};

			scope.removeLink = function(index) {
				for (index = index + 1; index < Object.keys(scope.links).length; index++) {
					scope.links[index] = scope.links[index + 1]
				}
				delete scope.links[index];
			};
		}
	};
});
