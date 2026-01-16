const allFactoriesData = {
    "Factory A": {
        "Process Section 1": {
            "process_name": "Build Process",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Warm pressing machine",
                    "work_type_desc": "NVA - Warm pressing machine",
                    "work_type": "NVA",
                    "times": {
                        "Setup Parts": 5
                    },
                    "total_time": 5
                },
                {
                    "task_name": "Clean press tool",
                    "work_type_desc": "NNVA - Clean press tool",
                    "work_type": "NNVA",
                    "times": {
                        "Setup Parts": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Setup next pressings",
                    "work_type_desc": "NNVA - Setup next pressings",
                    "work_type": "NNVA",
                    "times": {
                        "Setup Parts": 5
                    },
                    "total_time": 5
                },
                {
                    "task_name": "Align rivnuts",
                    "work_type_desc": "NNVA - Align rivnuts",
                    "work_type": "NNVA",
                    "times": {
                        "Setup Parts": 9
                    },
                    "total_time": 9
                },
                {
                    "task_name": "Align studs",
                    "work_type_desc": "NNVA - Align studs",
                    "work_type": "NNVA",
                    "times": {
                        "Setup Parts": 9
                    },
                    "total_time": 9
                },
                {
                    "task_name": "Load plate",
                    "work_type_desc": "VA - Load plate",
                    "work_type": "VA",
                    "times": {
                        "Setup Parts": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Activate press",
                    "work_type_desc": "VA - Activate press",
                    "work_type": "VA",
                    "times": {
                        "Produce Parts": 6
                    },
                    "total_time": 6
                },
                {
                    "task_name": "Deactivate press",
                    "work_type_desc": "NNVA - Deactivate press",
                    "work_type": "NNVA",
                    "times": {
                        "Produce Parts": 9
                    },
                    "total_time": 9
                },
                {
                    "task_name": "Remove plate",
                    "work_type_desc": "VA - Remove plate",
                    "work_type": "VA",
                    "times": {
                        "Produce Parts": 8
                    },
                    "total_time": 8
                },
                {
                    "task_name": "Inspect plate",
                    "work_type_desc": "VA - Inspect plate",
                    "work_type": "VA",
                    "times": {
                        "Produce Parts": 7
                    },
                    "total_time": 7
                },
                {
                    "task_name": "Package plate",
                    "work_type_desc": "VA - Package plate",
                    "work_type": "VA",
                    "times": {
                        "Produce Parts": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Buff surface",
                    "work_type_desc": "VA - Buff surface",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 23
                    },
                    "total_time": 23
                },
                {
                    "task_name": "Mount front wheel",
                    "work_type_desc": "VA - Mount front wheel",
                    "work_type": "VA",
                    "times": {
                        "Mount Wheels": 21
                    },
                    "total_time": 21
                },
                {
                    "task_name": "Mount rear wheel",
                    "work_type_desc": "VA - Mount rear wheel",
                    "work_type": "VA",
                    "times": {
                        "Mount Wheels": 21
                    },
                    "total_time": 21
                },
                {
                    "task_name": "Attach left bracket",
                    "work_type_desc": "VA - Attach left bracket",
                    "work_type": "VA",
                    "times": {
                        "Attach Bracket": 30
                    },
                    "total_time": 30
                },
                {
                    "task_name": "Attach right bracket",
                    "work_type_desc": "VA - Attach right bracket",
                    "work_type": "VA",
                    "times": {
                        "Attach Bracket": 31
                    },
                    "total_time": 31
                },
                {
                    "task_name": "Assemble gear 1",
                    "work_type_desc": "VA - Assemble gear 1",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 24
                    },
                    "total_time": 24
                },
                {
                    "task_name": "Assemble gear 2",
                    "work_type_desc": "VA - Assemble gear 2",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 25
                    },
                    "total_time": 25
                },
                {
                    "task_name": "Assemble main shaft",
                    "work_type_desc": "VA - Assemble main shaft",
                    "work_type": "VA",
                    "times": {
                        " Shaft Assembly": 28
                    },
                    "total_time": 28
                },
                {
                    "task_name": "Assemble secondary shaft",
                    "work_type_desc": "VA - Assemble secondary shaft",
                    "work_type": "VA",
                    "times": {
                        " Shaft Assembly": 28
                    },
                    "total_time": 28
                }
            ],
            "stations": [
                "Setup Parts",
                "Produce Parts",
                "Buff Three Parts",
                "Mount Wheels",
                "Attach Bracket",
                "Gear Assembly",
                " Shaft Assembly"
            ]
        },
        "Process Section 2": {
            "process_name": "Assembly Process",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Prepare components",
                    "work_type_desc": "NNVA - Prepare components",
                    "work_type": "NNVA",
                    "times": {
                        "Station 1": 15
                    },
                    "total_time": 15
                },
                {
                    "task_name": "Inspect components",
                    "work_type_desc": "VA - Inspect components",
                    "work_type": "VA",
                    "times": {
                        "Station 1": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Assemble frame",
                    "work_type_desc": "VA - Assemble frame",
                    "work_type": "VA",
                    "times": {
                        "Station 2": 25
                    },
                    "total_time": 25
                },
                {
                    "task_name": "Install motor",
                    "work_type_desc": "VA - Install motor",
                    "work_type": "VA",
                    "times": {
                        "Station 2": 20
                    },
                    "total_time": 20
                },
                {
                    "task_name": "Connect wiring",
                    "work_type_desc": "VA - Connect wiring",
                    "work_type": "VA",
                    "times": {
                        "Station 3": 18
                    },
                    "total_time": 18
                },
                {
                    "task_name": "Test connections",
                    "work_type_desc": "VA - Test connections",
                    "work_type": "VA",
                    "times": {
                        "Station 3": 12
                    },
                    "total_time": 12
                },
                {
                    "task_name": "Final assembly",
                    "work_type_desc": "VA - Final assembly",
                    "work_type": "VA",
                    "times": {
                        "Station 4": 30
                    },
                    "total_time": 30
                },
                {
                    "task_name": "Quality check",
                    "work_type_desc": "VA - Quality check",
                    "work_type": "VA",
                    "times": {
                        "Station 4": 15
                    },
                    "total_time": 15
                }
            ],
            "stations": [
                "Station 1",
                "Station 2",
                "Station 3",
                "Station 4"
            ]
        },
        "Process Section 3": {
            "process_name": "Packaging Process",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Clean product",
                    "work_type_desc": "NNVA - Clean product",
                    "work_type": "NNVA",
                    "times": {
                        "Packaging": 8
                    },
                    "total_time": 8
                },
                {
                    "task_name": "Wrap product",
                    "work_type_desc": "VA - Wrap product",
                    "work_type": "VA",
                    "times": {
                        "Packaging": 12
                    },
                    "total_time": 12
                },
                {
                    "task_name": "Label product",
                    "work_type_desc": "VA - Label product",
                    "work_type": "VA",
                    "times": {
                        "Packaging": 5
                    },
                    "total_time": 5
                },
                {
                    "task_name": "Box product",
                    "work_type_desc": "VA - Box product",
                    "work_type": "VA",
                    "times": {
                        "Packaging": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Seal box",
                    "work_type_desc": "VA - Seal box",
                    "work_type": "VA",
                    "times": {
                        "Packaging": 7
                    },
                    "total_time": 7
                },
                {
                    "task_name": "Apply shipping label",
                    "work_type_desc": "VA - Apply shipping label",
                    "work_type": "VA",
                    "times": {
                        "Packaging": 6
                    },
                    "total_time": 6
                }
            ],
            "stations": [
                "Packaging"
            ]
        },
        "SCU1": {
            "process_name": "SCU1name",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [],
            "stations": []
        }
    },
    "Factory B": {
        "Process Section 1": {
            "process_name": "Manufacturing Process",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Raw material inspection",
                    "work_type_desc": "VA - Raw material inspection",
                    "work_type": "VA",
                    "times": {
                        "Inspection": 20
                    },
                    "total_time": 20
                },
                {
                    "task_name": "Cut material",
                    "work_type_desc": "VA - Cut material",
                    "work_type": "VA",
                    "times": {
                        "Cutting": 35
                    },
                    "total_time": 35
                },
                {
                    "task_name": "Drill holes",
                    "work_type_desc": "VA - Drill holes",
                    "work_type": "VA",
                    "times": {
                        "Drilling": 28
                    },
                    "total_time": 28
                },
                {
                    "task_name": "Weld parts",
                    "work_type_desc": "VA - Weld parts",
                    "work_type": "VA",
                    "times": {
                        "Welding": 40
                    },
                    "total_time": 40
                },
                {
                    "task_name": "Grind edges",
                    "work_type_desc": "NNVA - Grind edges",
                    "work_type": "NNVA",
                    "times": {
                        "Finishing": 15
                    },
                    "total_time": 15
                },
                {
                    "task_name": "Paint parts",
                    "work_type_desc": "VA - Paint parts",
                    "work_type": "VA",
                    "times": {
                        "Finishing": 25
                    },
                    "total_time": 25
                }
            ],
            "stations": [
                "Inspection",
                "Cutting",
                "Drilling",
                "Welding",
                "Finishing"
            ]
        },
        "Process Section 2": {
            "process_name": "Quality Control",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Visual inspection",
                    "work_type_desc": "VA - Visual inspection",
                    "work_type": "VA",
                    "times": {
                        "QC Station 1": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Dimension check",
                    "work_type_desc": "VA - Dimension check",
                    "work_type": "VA",
                    "times": {
                        "QC Station 1": 15
                    },
                    "total_time": 15
                },
                {
                    "task_name": "Weight measurement",
                    "work_type_desc": "VA - Weight measurement",
                    "work_type": "VA",
                    "times": {
                        "QC Station 2": 8
                    },
                    "total_time": 8
                },
                {
                    "task_name": "Stress test",
                    "work_type_desc": "VA - Stress test",
                    "work_type": "VA",
                    "times": {
                        "QC Station 2": 30
                    },
                    "total_time": 30
                },
                {
                    "task_name": "Documentation",
                    "work_type_desc": "NNVA - Documentation",
                    "work_type": "NNVA",
                    "times": {
                        "QC Station 3": 12
                    },
                    "total_time": 12
                },
                {
                    "task_name": "Final approval",
                    "work_type_desc": "VA - Final approval",
                    "work_type": "VA",
                    "times": {
                        "QC Station 3": 5
                    },
                    "total_time": 5
                }
            ],
            "stations": [
                "QC Station 1",
                "QC Station 2",
                "QC Station 3"
            ]
        }
    },
    "Factory C": {
        "Process Section 1": {
            "process_name": "Production Line 1",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Load raw materials",
                    "work_type_desc": "NNVA - Load raw materials",
                    "work_type": "NNVA",
                    "times": {
                        "Line Start": 12
                    },
                    "total_time": 12
                },
                {
                    "task_name": "Process step 1",
                    "work_type_desc": "VA - Process step 1",
                    "work_type": "VA",
                    "times": {
                        "Process 1": 22
                    },
                    "total_time": 22
                },
                {
                    "task_name": "Process step 2",
                    "work_type_desc": "VA - Process step 2",
                    "work_type": "VA",
                    "times": {
                        "Process 2": 18
                    },
                    "total_time": 18
                },
                {
                    "task_name": "Process step 3",
                    "work_type_desc": "VA - Process step 3",
                    "work_type": "VA",
                    "times": {
                        "Process 3": 25
                    },
                    "total_time": 25
                },
                {
                    "task_name": "Unload finished goods",
                    "work_type_desc": "VA - Unload finished goods",
                    "work_type": "VA",
                    "times": {
                        "Line End": 10
                    },
                    "total_time": 10
                }
            ],
            "stations": [
                "Line Start",
                "Process 1",
                "Process 2",
                "Process 3",
                "Line End"
            ]
        },
        "Process Section 2": {
            "process_name": "Production Line 2",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Setup equipment",
                    "work_type_desc": "NNVA - Setup equipment",
                    "work_type": "NNVA",
                    "times": {
                        "Setup": 15
                    },
                    "total_time": 15
                },
                {
                    "task_name": "Operation 1",
                    "work_type_desc": "VA - Operation 1",
                    "work_type": "VA",
                    "times": {
                        "Operation": 20
                    },
                    "total_time": 20
                },
                {
                    "task_name": "Operation 2",
                    "work_type_desc": "VA - Operation 2",
                    "work_type": "VA",
                    "times": {
                        "Operation": 18
                    },
                    "total_time": 18
                },
                {
                    "task_name": "Operation 3",
                    "work_type_desc": "VA - Operation 3",
                    "work_type": "VA",
                    "times": {
                        "Operation": 22
                    },
                    "total_time": 22
                },
                {
                    "task_name": "Cleanup",
                    "work_type_desc": "NNVA - Cleanup",
                    "work_type": "NNVA",
                    "times": {
                        "Cleanup": 8
                    },
                    "total_time": 8
                }
            ],
            "stations": [
                "Setup",
                "Operation",
                "Cleanup"
            ]
        },
        "Process Section 3": {
            "process_name": "Production Line 3",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Initialize system",
                    "work_type_desc": "NNVA - Initialize system",
                    "work_type": "NNVA",
                    "times": {
                        "Init": 10
                    },
                    "total_time": 10
                },
                {
                    "task_name": "Run process A",
                    "work_type_desc": "VA - Run process A",
                    "work_type": "VA",
                    "times": {
                        "Process A": 30
                    },
                    "total_time": 30
                },
                {
                    "task_name": "Run process B",
                    "work_type_desc": "VA - Run process B",
                    "work_type": "VA",
                    "times": {
                        "Process B": 28
                    },
                    "total_time": 28
                },
                {
                    "task_name": "Run process C",
                    "work_type_desc": "VA - Run process C",
                    "work_type": "VA",
                    "times": {
                        "Process C": 25
                    },
                    "total_time": 25
                },
                {
                    "task_name": "Shutdown system",
                    "work_type_desc": "NNVA - Shutdown system",
                    "work_type": "NNVA",
                    "times": {
                        "Shutdown": 8
                    },
                    "total_time": 8
                }
            ],
            "stations": [
                "Init",
                "Process A",
                "Process B",
                "Process C",
                "Shutdown"
            ]
        }
    },
    "SCU": {
        "mainline": {
            "process_name": "mainline",
            "process_type": "Product",
            "measurement_method": "Measurement Method:",
            "time_unit": "secs",
            "takt_time": "Takt Time",
            "prepared_by": "Chris Coles",
            "process_data": [
                {
                    "task_name": "Warm pressing machine",
                    "work_type_desc": "NVA - Warm pressing machine",
                    "work_type": "NVA",
                    "times": {
                        "Produce Parts": 6
                    },
                    "total_time": 6,
                    "comments": ""
                },
                {
                    "task_name": "Setup next pressings",
                    "work_type_desc": "NNVA - Setup next pressings",
                    "work_type": "NNVA",
                    "times": {
                        "Produce Parts": 5
                    },
                    "total_time": 5,
                    "comments": ""
                },
                {
                    "task_name": "Load plate",
                    "work_type_desc": "VA - Load plate",
                    "work_type": "VA",
                    "times": {
                        "Produce Parts": 10
                    },
                    "total_time": 10,
                    "comments": ""
                },
                {
                    "task_name": "Align rivnuts",
                    "work_type_desc": "NNVA - Align rivnuts",
                    "work_type": "NNVA",
                    "times": {
                        "Gear Assembly": 9
                    },
                    "total_time": 9,
                    "comments": ""
                },
                {
                    "task_name": "Align studs",
                    "work_type_desc": "NNVA - Align studs",
                    "work_type": "NNVA",
                    "times": {
                        "Produce Parts": 9
                    },
                    "total_time": 9,
                    "comments": ""
                },
                {
                    "task_name": "Activate press",
                    "work_type_desc": "VA - Activate press",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 6
                    },
                    "total_time": 6,
                    "comments": ""
                },
                {
                    "task_name": "Deactivate press",
                    "work_type_desc": "NNVA - Deactivate press",
                    "work_type": "NNVA",
                    "times": {
                        "Mount Wheels": 9
                    },
                    "total_time": 9,
                    "comments": ""
                },
                {
                    "task_name": "Package plate",
                    "work_type_desc": "VA - Package plate",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 10
                    },
                    "total_time": 10,
                    "comments": ""
                },
                {
                    "task_name": "Buff surface",
                    "work_type_desc": "VA - Buff surface",
                    "work_type": "VA",
                    "times": {
                        "Setup Parts": 23
                    },
                    "total_time": 23,
                    "comments": ""
                },
                {
                    "task_name": "Mount front wheel",
                    "work_type_desc": "VA - Mount front wheel",
                    "work_type": "VA",
                    "times": {
                        "Mount Wheels": 21
                    },
                    "total_time": 21,
                    "comments": ""
                },
                {
                    "task_name": "Mount rear wheel",
                    "work_type_desc": "VA - Mount rear wheel",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 21
                    },
                    "total_time": 21,
                    "comments": ""
                },
                {
                    "task_name": "Attach left bracket",
                    "work_type_desc": "VA - Attach left bracket",
                    "work_type": "VA",
                    "times": {
                        "Attach Bracket": 30
                    },
                    "total_time": 30,
                    "comments": ""
                },
                {
                    "task_name": "Assemble gear 1",
                    "work_type_desc": "VA - Assemble gear 1",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 24
                    },
                    "total_time": 24,
                    "comments": ""
                },
                {
                    "task_name": "Assemble gear 2",
                    "work_type_desc": "VA - Assemble gear 2",
                    "work_type": "VA",
                    "times": {
                        "Gear Assembly": 25
                    },
                    "total_time": 25,
                    "comments": ""
                },
                {
                    "task_name": "Assemble main shaft",
                    "work_type_desc": "VA - Assemble main shaft",
                    "work_type": "VA",
                    "times": {
                        " Shaft Assembly": 28
                    },
                    "total_time": 28,
                    "comments": ""
                },
                {
                    "task_name": "Assemble secondary shaft",
                    "work_type_desc": "VA - Assemble secondary shaft",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 28
                    },
                    "total_time": 28,
                    "comments": ""
                },
                {
                    "task_name": "Assembly1",
                    "work_type_desc": "NVA - Assembly1",
                    "work_type": "NVA",
                    "times": {
                        "Setup Parts": 7
                    },
                    "total_time": 7,
                    "comments": ""
                },
                {
                    "task_name": "Attach right bracket.1",
                    "work_type_desc": "VA - Attach right bracket.1",
                    "work_type": "VA",
                    "times": {
                        "Mount Wheels": 11
                    },
                    "total_time": 11,
                    "comments": ""
                },
                {
                    "task_name": "Inspect plate1",
                    "work_type_desc": "VA - Inspect plate1",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 15
                    },
                    "total_time": 15,
                    "comments": ""
                },
                {
                    "task_name": "test1.2",
                    "work_type_desc": "NVA - test1.2",
                    "work_type": "NVA",
                    "times": {
                        "Buff Three Parts": 8
                    },
                    "total_time": 8,
                    "comments": ""
                },
                {
                    "task_name": "Attach right bracket.1",
                    "work_type_desc": "VA - Attach right bracket.1",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 9
                    },
                    "total_time": 9,
                    "comments": ""
                },
                {
                    "task_name": "Attach right bracket.2",
                    "work_type_desc": "VA - Attach right bracket.2",
                    "work_type": "VA",
                    "times": {
                        "Buff Three Parts": 11
                    },
                    "total_time": 11,
                    "comments": ""
                }
            ],
            "stations": [
                "Produce Parts",
                "Gear Assembly",
                "Mount Wheels",
                "Buff Three Parts",
                "Setup Parts",
                "Attach Bracket",
                " Shaft Assembly"
            ]
        }
    }
};