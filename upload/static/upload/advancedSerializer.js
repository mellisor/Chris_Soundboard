
function serializeById(id) {
    var item = document.getElementById(id);
    var dict = serializeDict({},item);
    return dict;
}

// Serializes all elements in items, if there is a div inside with className 'inputList'
// an attribute with the div's name attribute will be created with value of an array containing
// all input attributes inside of it
function serializeDict(curr,elem) {
    var nodes = elem.childNodes;
    nodes.forEach(function(item) {
        if( item.tagName == "INPUT" || item.tagName == "TEXTAREA") {
            if (item.getAttribute("type") == "checkbox") {
                if (item.checked) {
                    curr[item.getAttribute("name")] = item.checked;
                }
            }
            else if (item.getAttribute("type") == "radio") {
                if(item.checked) {
                    console.log("CHECKED");
                    curr[item.getAttribute("name")] = item.value;
                }
                else if (!curr[item.getAttribute("name")]) {
                    curr[item.getAttribute("name")] = null;
                }
            }
            else {
                curr[item.getAttribute("name")] = item.value;
            }
        }
        else if (item.tagName == "SELECT") {
            var selected = [];
            for (var i = 0; i < item.options.length; i++) {
                if (item.options[i].selected) {
                    selected.push(item.options[i].value);
                }
            }
            curr[item.getAttribute("name")] = selected;
        }
        else if (item.tagName == "DIV" && item.className == "inputList") {
            var list = [];
            item.childNodes.forEach(function(child) {
                list.push(serializeDict({},child));
            });
            var actualList = [];
            for (var i = 0; i < list.length; i++) {
                if(Object.entries(list[i]).length != 0) {
                    actualList.push(list[i])
                }
            }
            curr[item.getAttribute("name")] = actualList;
        }
        else {
            return serializeDict(curr,item);
        }
    })
    return curr;
}