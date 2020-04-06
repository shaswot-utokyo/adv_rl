EXP_PARAMS = {
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# utility_v0_T24, and gamma
    'utility_v0_T240-g90': { 
        'env_name':         "utility_v0_T240",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# sparse_v0_T24_1x, T24 and gamma
     'sparse_v0_T24_1x-g90': { 
        'env_name':         "sparse_v0_T24_1x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
    'sparse_v0_T24_1x-g95': { 
        'env_name':         "sparse_v0_T24_1x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95, 
        'batch_size':       32
    },
    'sparse_v0_T24_1x-g97': { 
        'env_name':         "sparse_v0_T24_1x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97, 
        'batch_size':       32
    },
    'sparse_v0_T24_1x-g99': { 
        'env_name':         "sparse_v0_T24_1x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, 
        'batch_size':       32
    },
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# sparse_v0_T24_4x, T24 and gamma
     'sparse_v0_T24_4x-g90': { 
        'env_name':         "sparse_v0_T24_4x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
    'sparse_v0_T24_4x-g95': { 
        'env_name':         "sparse_v0_T24_4x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95, 
        'batch_size':       32
    },
    'sparse_v0_T24_4x-g97': { 
        'env_name':         "sparse_v0_T24_4x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97, 
        'batch_size':       32
    },
    'sparse_v0_T24_4x-g99': { 
        'env_name':         "sparse_v0_T24_4x",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, 
        'batch_size':       32
    },
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# hard_v1 , T120 and gamma
    'hard_v1_T120-g90': { 
        'env_name':         "hard_v1_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90,  
        'batch_size':       32
    },
    'hard_v1_T120-g95': { 
        'env_name':         "hard_v1_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95,  
        'batch_size':       32
    },
     'hard_v1_T120-g97': { 
        'env_name':         "hard_v1_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97,  
        'batch_size':       32
    },

    'hard_v1_T120-g99': { 
        'env_name':         "hard_v1_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99,  
        'batch_size':       32
    },

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# hard_env_v1, T24, and gamma
    'hard_v1_T24-g90': { 
        'env_name':         "hard_v1_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
    'hard_v1_T24-g95': { 
        'env_name':         "hard_v1_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95, 
        'batch_size':       32
    },
    'hard_v1_T24-g97': { 
        'env_name':         "hard_v1_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97, 
        'batch_size':       32
    },  
    'hard_v1_T24-g99': { 
        'env_name':         "hard_v1_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, 
        'batch_size':       32
    },  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# hard_env_v0, T24, and gamma
    'hard_v0_T24-g90': { 
        'env_name':         "hard_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
    'hard_v0_T24-g95': { 
        'env_name':         "hard_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95, 
        'batch_size':       32
    },
    'hard_v0_T24-g97': { 
        'env_name':         "hard_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97, 
        'batch_size':       32
    },  
    'hard_v0_T24-g99': { 
        'env_name':         "hard_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, 
        'batch_size':       32
    },  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# T120 and gamma
    'eno_v0_T120-g90': { 
        'env_name':         "eno_v0_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90,  
        'batch_size':       32
    },
    'eno_v0_T120-g95': { 
        'env_name':         "eno_v0_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95,
        'batch_size':       32
    },
    'eno_v0_T120-g9791': { 
        'env_name':         "eno_v0_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9791, # eqv to g90@T24 
        'batch_size':       32
    },
    'eno_v0_T120-g9898': { 
        'env_name':         "eno_v0_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9898, # eqv to g95@T24 
        'batch_size':       32
    },
    'eno_v0_T120-g9939': { 
        'env_name':         "eno_v0_T120",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    10,        # rollout by 2hrs=10steps
        'replay_size':      120*365*2, # 2 years
        'replay_initial':   120*10,    # 10 days
        'target_net_sync':  120*10,    # 10 days
        'epsilon_frames':   120*30*6,  # 6 months
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9939, # eqv to g97@T24 
        'batch_size':       32
    },
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# T24 and gamma
    'eno_v0_T24-g90': { 
        'env_name':         "eno_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.90, 
        'batch_size':       32
    },
    'eno_v0_T24-g95': { 
        'env_name':         "eno_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.95, 
        'batch_size':       32
    },
    'eno_v0_T24-g97': { 
        'env_name':         "eno_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.97, 
        'batch_size':       32
    },
    'eno_v0_T24-g98': { 
        'env_name':         "eno_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.98, 
        'batch_size':       32
    },
    'eno_v0_T24-g99': { 
        'env_name':         "eno_v0_T24",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32,
        'rollout_steps':    2,        # rollout by 2hrs=2steps
        'replay_size':      24*365*2, # 240*365*2/10,
        'replay_initial':   24*10,    # 240*10/10,
        'target_net_sync':  24*10,    # 240*10/10,
        'epsilon_frames':   24*30*6,  # 240*30*6/10,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, 
        'batch_size':       32
    },
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

}
