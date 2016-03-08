app.directive('scmsContentEdit', function($compile){
	return {
		restrict: 'E',
		scope: {
			layer: "=",
			content: "="
		},
		templateUrl: "/html/directives/scms-content-edit.tpl.html",
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
