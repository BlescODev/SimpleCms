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
				pre: function(scope) {},
				post: function(scope, iElement) {
					$compile(contents)(scope, function(clone) {
						iElement.append(clone);
					});
				}
			};
		}
	};
});
