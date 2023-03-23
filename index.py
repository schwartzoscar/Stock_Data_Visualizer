import app, api, ui, graph, error

def main():
    #Call function in ui.py that begins the interaction between the user and system
    print("Stock Data Visualizer\n--------------------")
    app.SetStockSymbol(ui.get_stock_symbol())
    app.SetChartType(ui.get_chart_type())
    app.SetTimeSeries(ui.get_time_series())
    app.SetDates(ui.get_dates()[0],  ui.get_dates()[1])
    
    if (app.GetChartType() == "Bar"): graph.create_bar_graph()
    else: graph.create_line_graph()

    if not ui.restart_program():
            #break
            return
    return
main()