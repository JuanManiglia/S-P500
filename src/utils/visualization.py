# Imports
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib import RcParams, rcParams
import plotly_express as px
import squarify
import plotly

#Config Parametros de visualización de datos 
sns.set_style("white")
sns.set_context('notebook')
sns.set_style("ticks")
sns.set(rc={"figure.dpi":300, "savefig.dpi": 300})


class Viz:
    
    """
    Esta clase se usa para construir todo tipo de gráficos.
    """
    @staticmethod
    def draw_treemap(df, path, color, values, title, filename, html_path, save=False):
        '''
        Esta función dibuja un mapa de colores basado en datos numéricos.
        Se utiliza para ver la jerarquía de datos.
        Parámetros: 
            - df: Un pandas Dataframe.
            - path: Una lista con la jerarquía que estará representada.
            - color: El valor que asignará el color.
            - values: Los valores que se estructurarán.
            - title: Título.
            - filename: El nombre del archivo para guardarlo.
            - html_path: El directorio en el que se guardará.
            - save: Un bool. Si True, guardará el gráfico en html y .png (Por Defecto =  False)
        ''' 
        doc_name = html_path + filename + '.html'
        fig = px.treemap(
        df,
        path= path,
        color=color,
        values=values,
        title=title,
        color_continuous_scale=["#FFB533", "#000000", "#E60909"]
    )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='Helvetica',
        )

        if save:
            plotly.offline.plot(fig, filename=doc_name)
            
        fig.show()

    @staticmethod
    def draw_sunburst(df, path, color, values, title, html_path, save=False, filename=None):
        '''
        Esta función dibuja un mapa de colores basado en datos numéricos.
        Se utiliza para ver la jerarquía de datos.
        Parámetros: 
            - df: Un pandas Dataframe.
            - path: Una lista con la jerarquía que estará representada.
            - color: El valor que asignará el color.
            - values: Los valores que se estructurarán.
            - title: Titulo.
            - filename: El nombre del archivo para guardarlo.
            - html_path: el directorio en el que se guardará en html
            - save: Un bool. Si True, guardará el gráfico en html y .png (Por Defecto =  False)
        ''' 
        doc_name = html_path + filename + '.html'
        fig = px.sunburst(
        df,
        path= path,
        color=color,
        values=values,
        title=title,
        color_continuous_scale=["#FFB533", "#000000", "#E60909"]
    )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='Helvetica',
        )

        if save:
            plotly.offline.plot(fig, filename=doc_name)
            
        fig.show()

    @staticmethod
    def draw_heatmap(df_corr, title, path, filename=None, save=False, ):
        '''
        Esta función dibuja un mapa de calor.
        Parámetros:
            - df: U pandas DataFrame con el metodo de corr().
            - title: Titulo
            - path: El path donde se guardará.
            - save: Si True, se guardará.
        ''' 
        plt.figure(figsize=(15, 15))
        fig = sns.heatmap(df_corr,
        center=0,
        square= True,
        linewidths = .3,
        robust=True,
        cmap=sns.cm.mako_r
        )

        
        fig.set_title(title, fontdict= {'fontsize': 24, 'fontweight': 'bold'}, y=1.1);

        if save:
            doc_name = path + filename + '.png'
            plt.savefig(doc_name)

    @staticmethod
    def draw_barplot(df, x, y, title, path, filename=None, save=False):
        '''
        Esta función dibuja un diagrama de barras
        Parámetros:
            - df: Un pandas DataFrame.
            - x: Eje x.
            - y: Eje y.
            - title: Titulo.
            - path: El path donde se guardará.
            - filename: Nombre del archivo file. (Por Defecto = None).
            - save: Si True, Guarda el grafico.
        '''

        fig = px.bar(
            df,
            x=x, 
            y=y, 
            title=title
        )

        fig.update_layout(
                        title_font_size=36,
                        title_font_family='<b>Helvetica</b>',
                        font=dict(
                            family='Helvetica',
                            size=12
                        )

        )
        
        fig.update_traces(
        marker_color= '#FFB533'
        )

        if save:
            doc_name = path + filename + '.html'

            plotly.offline.plot(fig, filename=doc_name)

        fig.show()

    @staticmethod
    def draw_histogram(df, x, y, title, filename=None, path=None, save=False):
        '''
        Esta función dibuja un histograma.
        Parámetros:
            - df: Un pandas Dataframe
            - x: Eje x.
            - y: Eje y.
            - title: Titulo.
            - filename: El nombre del archivo.
            - path: El path donde se guardará.
            - save: Si true, se guardará
        '''
        fig = px.histogram(
            df, 
            x=x, 
            y=y,
            title=title
        )

        fig.update_layout(
            title_font_size=36,
            title_font_family='<b>Helvetica</b>',
            font=dict(
                family='Helvetica',
                size=12
            )
        )

        fig.update_traces(
            marker_color= '#FFB533'
            )

        if save:
            doc_name = path + filename + '.html'

            plotly.offline.plot(fig, filename=doc_name)

        fig.show()

    @staticmethod
    def draw_violinplot(df, col, title, path=None, filename=None, save=False):
        '''
        Esta función dibuja una trama de violín.
        Parámetros:
            - df: Un pandas Dataframe
            - col: La columna del Dataframe.
            - title: Titulo.
            - path: El path donde se guardará.
            - filename: El nombre del archivo.
            - save: Si True, se guardará
        '''
        plt.figure(figsize=(10, 5))
        fig = sns.violinplot(df[col],
        linewidths = .3,
        robust=True,
        cmap=sns.cm.mako_r
        )
        fig.set_title(title, fontdict= {'fontsize': 24, 'fontweight': 'bold'}, y=1);


        if save:
            doc_name = path + filename + '.png'
            plt.savefig(doc_name)
    
    @staticmethod
    def draw_time_series(df, path=None, filename=None, save=False):
        '''
        Esta función dibuja dos series temporales una con el precio maximo y minimo y la otra con el volumen.
        Parámetros:
            - df: Un pandas Dataframe
            - title: Titulo.
            - path: El path donde se guardará.
            - filename: El nombre del archivo.
            - save: Si True, se guardará
        '''
        # First Subplot
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
        ax1.plot(df["fecha"], df["cierre"])
        ax1.set_xlabel("fecha", fontsize=12)
        ax1.set_ylabel("Stock precio")
        ax1.set_title("cierre history")

        # Second Subplot
        ax1.plot(df["fecha"], df["maximo"], color="green")
        ax1.set_xlabel("fecha", fontsize=12)
        ax1.set_ylabel("Stock precio")
        ax1.set_title("precio maximo History")

        # Third Subplot
        ax1.plot(df["fecha"], df["minimo"], color="red")
        ax1.set_xlabel("fecha", fontsize=12)
        ax1.set_ylabel("Stock precio")
        ax1.set_title("precio minimo History")

        # Fourth Subplot
        ax2.plot(df["fecha"], df["volumen"], color="orange")
        ax2.set_xlabel("fecha", fontsize=12)
        ax2.set_ylabel("Stock precio")
        ax2.set_title("Volumen History")

        if save:
            doc_name = path + filename + '.png'
            plt.savefig(doc_name)
