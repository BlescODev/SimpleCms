app.directive('layer', function($compile){
	return {
		restrict: 'E',
		scope: {
			level: "=",
			content: "="
		},
		templateUrl: "/html/directives/layer.tpl.html",
		compile: function(tElement, tAttr) {
			var contents = tElement.contents().remove();
			var compiledContents;

			return function(scope, iElement, iAttr) {
				if(!compiledContents) {
					compiledContents = $compile(contents);
				}
				compiledContents(scope, function(clone, scope) {
					iElement.append(clone); 
				});
			};
		}
	};
});
