app.directive('scmsContentEdit', function($compile) {
	return {
		restrict: 'E',
		scope: {
			layer: "=",
			content: "="
		},
		templateUrl: "/html/directives/scms-content-edit.tpl.html",
		compile: function(tElement) {
			var contents = tElement.contents().remove();
			return {
				pre: function(scope) {
					scope.resize = function() {
						var ta = document.getElementById("ta");
						ta.style.height = 'auto';
						ta.style.height = ta.scrollHeight + 'px';
					}
				},
				post: function(scope, iElement) {
					$compile(contents)(scope, function(clone) {
						iElement.append(clone);
					});
				}
			};
		}
	};
});
