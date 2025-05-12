class JupyterEcharts:
    """
    credit: https://gist.github.com/drorhilman/c5ae2f5d6661ea12fd2b5d0c078f9700
    """
    
    ECHARTS_CDN = "https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min"
    ECHARTS_REQUIREJS_CONF = f"requirejs.config({{paths: {{echarts: '{ECHARTS_CDN}',}}}});"
    ECHARTS_TEMPLATE = f"""
        <div id="{{ID}}" style="width: {{WIDTH}};height:{{HEIGHT}};"></div>
        <script type="module">
        {ECHARTS_REQUIREJS_CONF}    
        requirejs(["echarts"], (echarts) => {{
                        let myChart = echarts.init(document.getElementById('{{ID}}'));
                        myChart.setOption({{OPTION}});
                }}
            )
        </script>
    """
    
    @staticmethod
    def _multi_replace(string: str, replacements: dict):
        for k, v in replacements.items():
            string = string.replace(k, v)
        return string
    
    @staticmethod
    def _echarts(option: dict, width="800px", height="500px", id='chart'):
        import json
        from IPython.display import HTML
        
        option = json.dumps(option)
        h = JupyterEcharts._multi_replace(
            JupyterEcharts.ECHARTS_TEMPLATE, {
                "{WIDTH}": width,
                "{HEIGHT}": height,
                "{OPTION}": option,
                "{ID}": id
            }
        )
        
        return HTML(h)
    
    @staticmethod
    def show(option, width="800px", height="800px") -> None:
        return JupyterEcharts._echarts(option, width, height)
