
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    exportEnabled: true,
    title:{
        text: "Temperature in Toronto - July 2017"
    },
    axisY: {
        title: "Temperature (°C)",
        suffix: " °C"
    },
    axisX: {
        valueFormatString: "DD MMMM"
    },
    data: [
    {
        type: "rangeArea",
        xValueFormatString: "DD MMMM", 
        yValueFormatString: "#0.## °C",
        toolTipContent: " <span style=\"color:#4F81BC\">{x}</span><br><b>Min:</b> {y[0]}<br><b>Max:</b> {y[1]}",
        dataPoints: [
            { x: new Date(2017,06,01), y:[15, 21] },
            { x: new Date(2017,06,02), y:[13, 27] },
            { x: new Date(2017,06,03), y:[14, 23] },
            { x: new Date(2017,06,04), y:[17, 25] },
            { x: new Date(2017,06,05), y:[16, 23] },
            { x: new Date(2017,06,06), y:[16, 29] },
            { x: new Date(2017,06,07), y:[18, 27] },
            { x: new Date(2017,06,08), y:[16, 25] },
            { x: new Date(2017,06,09), y:[15, 25] },
            { x: new Date(2017,06,10), y:[16, 23] },
            { x: new Date(2017,06,11), y:[15, 26] },
            { x: new Date(2017,06,12), y:[19, 23] },
            { x: new Date(2017,06,13), y:[16, 19] },
            { x: new Date(2017,06,14), y:[16, 27] },
            { x: new Date(2017,06,15), y:[18, 27] },
            { x: new Date(2017,06,16), y:[17, 24] },
            { x: new Date(2017,06,17), y:[19, 23] },
            { x: new Date(2017,06,18), y:[19, 26] },
            { x: new Date(2017,06,19), y:[20, 30] },
            { x: new Date(2017,06,20), y:[17, 21] },
            { x: new Date(2017,06,21), y:[19, 30] },
            { x: new Date(2017,06,22), y:[21, 23] },
            { x: new Date(2017,06,23), y:[20, 24] },
            { x: new Date(2017,06,24), y:[17, 22] },
            { x: new Date(2017,06,25), y:[17, 22] },
            { x: new Date(2017,06,26), y:[16, 22] },
            { x: new Date(2017,06,27), y:[19, 26] },
            { x: new Date(2017,06,28), y:[18, 23] },
            { x: new Date(2017,06,29), y:[18, 27] },
            { x: new Date(2017,06,30), y:[20, 31] },
            { x: new Date(2017,06,31), y:[19, 27] }
        ]
    }]
});
chart.render();

}