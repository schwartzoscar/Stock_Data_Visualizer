import app, api, ui, graph, error

def main():
    while True:
        #Call function in ui.py that begins the interaction between the user and system
        print("Stock Data Visualizer\n--------------------")
        app.SetStockSymbol(ui.get_stock_symbol())
        app.SetChartType(ui.get_chart_type())
        app.SetTimeSeries(ui.get_time_series())
        app.SetDates(ui.get_dates())
        api.pullStock()

        try:
            if (app.GetChartType() == "Bar"): graph.create_bar_graph()
            else: graph.create_line_graph()
        except ValueError:
            print("Can not find data for this symbol. Please try again.\n\n")
            continue

        if not ui.restart_program():
                break
    return
main()
