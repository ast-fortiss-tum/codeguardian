// From JSVulnerabilityDataSet, row no. 4444 .

console.mouseup(function() {
    var top,
        isSelection = '' + window.getSelection();
    
    if (!isSelection) {
        top        = console.scrollTop();
        
        Console.focus();
        console.scrollTop(top);
    }
});