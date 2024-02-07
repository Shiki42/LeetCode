window.copier = window.copier || {};
(function () {
    window.copier.init = function() {
        window.addRule = function() {
            var rulesDiv = document.getElementById('rules');
            var lastRule = rulesDiv.lastElementChild.cloneNode(true);
            rulesDiv.appendChild(lastRule);
        }
    }
    var addRuleBtn = document.getElementById('addRuleBtn');

    addRuleBtn.addEventListener('click', window.addRule);
})();