import os
import sys
import pdfkit
from pandas.io.excel import ExcelWriter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

"""
input excel files are generated from matchbox using a testrun id
another way could be is to use the TRID directly and extract the events from DB
"""

#######################################################################################################################
# definitions
# data mining sheets for regression

sw1_location = r"D:\HONDA\Regression\inputs\endurance_data\SW_HA22.00.09.02.1.001\events_8251.xlsx"
SW1 = "SW_HA22.00.09.02.1.001"

sw2_location = r"D:\HONDA\Regression\inputs\endurance_data\SW_HA22.00.09.02.1.005\events_8367.xlsx"
SW2 = "SW_HA22.00.09.02.1.005"

# endurance events list
endurance_event_types = ['AcuteDynamicWarningPed', 'AcuteDynamicWarningCrossing', 'PreDynamicWarningPed',
                         'PreDynamicWarningVeh', 'AutonomousBrakingL2Crossing', 'PreDynamicWarningCrossing',
                         'AcuteDynamicWarningVeh']


# eba uc output dictionary
# out_dict = {
#             "testcase1":
#             {
#             "tested": 10,
#             "passed_prebrake": 2,
#             "passed_prefill": 2
#             },
#             "testcase2":
#             {
#             "tested": 10,
#             "passed_prebrake": 2,
#             "passed_prefill": 2
#             }
#             }

# eba endurance output dictionary
eba_end_out = {"EVENT": [],
               SW1: [],
               SW2: []
               }


# recs overview
eba_recs_overview = {SW1: [],
                     SW2: [],
                     "OVERLAPPING_RECS": []
}


#######################################################################################################################
def regression_report():
    """
    using data mining excel sheet from matchbox which contains all the events
    create regression report for overlapping recs
    :return:
    """

    # load datas from data mining sheet
    # df1 = pd.read_csv(sw1_location, sep=';', delimiter=None)
    df1 = pd.read_excel(sw1_location)
    unique_event_types_1 = df1["Event Type"].unique()

    df2 = pd.read_excel(sw2_location)
    unique_event_types_2 = df2["Event Type"].unique()

    # creating recs stats and adding in the dictionary
    rec_names_1 = df1["Recording"].tolist()
    eba_recs_overview[SW1].append(len(rec_names_1))
    rec_names_2 = df2["Recording"].tolist()
    eba_recs_overview[SW2].append(len(rec_names_2))
    overlapping_recs = list(set(df1['Recording']).intersection(df2['Recording']))
    eba_recs_overview["OVERLAPPING_RECS"].append(len(overlapping_recs))

    for event_type in endurance_event_types:
        eba_end_out["EVENT"].append(event_type)
        sw1_events = 0
        sw2_events = 0
        for rec in overlapping_recs:
            if event_type in unique_event_types_1:
                no_of_events = len(df1.loc[df1['Recording'] == rec, 'Event Type'].values.tolist())
            else:
                no_of_events = 0
            #adding all sw1 events in one variable
            sw1_events += no_of_events

            if event_type in unique_event_types_2:
                no_of_events = len(df2.loc[df2['Recording'] == rec, 'Event Type'].values.tolist())
            else:
                no_of_events = 0
            # adding all sw2 events in one variable
            sw2_events += no_of_events

        eba_end_out[SW1].append(sw1_events)
        eba_end_out[SW2].append(sw2_events)

    df_output = pd.DataFrame(eba_end_out)
    df_recs_overview = pd.DataFrame(eba_recs_overview)

    fig = df_output.plot()
    fig.show()
    print()

    # fig1 = ff.create_table(df_output)
    # fig1.write_html("sw_comparison.html")
    #
    # fig2 = ff.create_table(df_recs_overview)
    # fig2.write_html("recs_overview.html")
    #
    # with open('p_graph.html', 'a') as f:
    #     f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
    #     f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))

if __name__ == "__main__":
    regression_report()
