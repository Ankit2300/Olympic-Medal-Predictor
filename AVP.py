{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cf6c98d8-199b-4127-b28c-36fb41ef64b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8e3c2da7-bf45-4def-929e-37b836700587",
   "metadata": {},
   "outputs": [],
   "source": [
    "teams = pd.read_csv(\"teams.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c5a3acef-46af-48c4-afc7-c82d91f159b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>events</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "      <th>prev_3_medals</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1964</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>22.0</td>\n",
       "      <td>161.0</td>\n",
       "      <td>64.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1968</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>23.2</td>\n",
       "      <td>170.2</td>\n",
       "      <td>70.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1972</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>29.0</td>\n",
       "      <td>168.3</td>\n",
       "      <td>63.8</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1980</td>\n",
       "      <td>11</td>\n",
       "      <td>11</td>\n",
       "      <td>23.6</td>\n",
       "      <td>168.4</td>\n",
       "      <td>63.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2004</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>18.6</td>\n",
       "      <td>170.8</td>\n",
       "      <td>64.8</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2139</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>25.0</td>\n",
       "      <td>179.0</td>\n",
       "      <td>71.1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2140</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2004</td>\n",
       "      <td>11</td>\n",
       "      <td>14</td>\n",
       "      <td>25.1</td>\n",
       "      <td>177.8</td>\n",
       "      <td>70.5</td>\n",
       "      <td>3</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2141</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2008</td>\n",
       "      <td>15</td>\n",
       "      <td>16</td>\n",
       "      <td>26.1</td>\n",
       "      <td>171.9</td>\n",
       "      <td>63.7</td>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2012</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>174.4</td>\n",
       "      <td>65.2</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2016</td>\n",
       "      <td>13</td>\n",
       "      <td>31</td>\n",
       "      <td>27.5</td>\n",
       "      <td>167.8</td>\n",
       "      <td>62.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2144 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team      country  year  events  athletes   age  height  weight  medals  \\\n",
       "0     AFG  Afghanistan  1964       8         8  22.0   161.0    64.2       0   \n",
       "1     AFG  Afghanistan  1968       5         5  23.2   170.2    70.0       0   \n",
       "2     AFG  Afghanistan  1972       8         8  29.0   168.3    63.8       0   \n",
       "3     AFG  Afghanistan  1980      11        11  23.6   168.4    63.2       0   \n",
       "4     AFG  Afghanistan  2004       5         5  18.6   170.8    64.8       0   \n",
       "...   ...          ...   ...     ...       ...   ...     ...     ...     ...   \n",
       "2139  ZIM     Zimbabwe  2000      19        26  25.0   179.0    71.1       0   \n",
       "2140  ZIM     Zimbabwe  2004      11        14  25.1   177.8    70.5       3   \n",
       "2141  ZIM     Zimbabwe  2008      15        16  26.1   171.9    63.7       4   \n",
       "2142  ZIM     Zimbabwe  2012       8         9  27.3   174.4    65.2       0   \n",
       "2143  ZIM     Zimbabwe  2016      13        31  27.5   167.8    62.2       0   \n",
       "\n",
       "      prev_medals  prev_3_medals  \n",
       "0             0.0            0.0  \n",
       "1             0.0            0.0  \n",
       "2             0.0            0.0  \n",
       "3             0.0            0.0  \n",
       "4             0.0            0.0  \n",
       "...           ...            ...  \n",
       "2139          0.0            0.0  \n",
       "2140          0.0            0.0  \n",
       "2141          3.0            1.0  \n",
       "2142          4.0            2.3  \n",
       "2143          0.0            2.3  \n",
       "\n",
       "[2144 rows x 11 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "48361655-962f-4f65-9701-4d78667275f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "teams = teams[[\"team\",\"country\",\"year\",\"athletes\",\"age\",\"medals\",\"prev_medals\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f786911f-2062-4ee1-ae94-9725b3558fc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1964</td>\n",
       "      <td>8</td>\n",
       "      <td>22.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1968</td>\n",
       "      <td>5</td>\n",
       "      <td>23.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1972</td>\n",
       "      <td>8</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1980</td>\n",
       "      <td>11</td>\n",
       "      <td>23.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2004</td>\n",
       "      <td>5</td>\n",
       "      <td>18.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2139</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2000</td>\n",
       "      <td>26</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2140</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2004</td>\n",
       "      <td>14</td>\n",
       "      <td>25.1</td>\n",
       "      <td>3</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2141</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2008</td>\n",
       "      <td>16</td>\n",
       "      <td>26.1</td>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2012</td>\n",
       "      <td>9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2016</td>\n",
       "      <td>31</td>\n",
       "      <td>27.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2144 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team      country  year  athletes   age  medals  prev_medals\n",
       "0     AFG  Afghanistan  1964         8  22.0       0          0.0\n",
       "1     AFG  Afghanistan  1968         5  23.2       0          0.0\n",
       "2     AFG  Afghanistan  1972         8  29.0       0          0.0\n",
       "3     AFG  Afghanistan  1980        11  23.6       0          0.0\n",
       "4     AFG  Afghanistan  2004         5  18.6       0          0.0\n",
       "...   ...          ...   ...       ...   ...     ...          ...\n",
       "2139  ZIM     Zimbabwe  2000        26  25.0       0          0.0\n",
       "2140  ZIM     Zimbabwe  2004        14  25.1       3          0.0\n",
       "2141  ZIM     Zimbabwe  2008        16  26.1       4          3.0\n",
       "2142  ZIM     Zimbabwe  2012         9  27.3       0          4.0\n",
       "2143  ZIM     Zimbabwe  2016        31  27.5       0          0.0\n",
       "\n",
       "[2144 rows x 7 columns]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f671bf9b-1baa-4063-a5e4-ecf6d06c25a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2144, 7)\n"
     ]
    }
   ],
   "source": [
    "print(teams.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ab30d263-5197-4a1a-bcef-7f25af903b3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['team', 'country', 'year', 'athletes', 'age', 'medals', 'prev_medals'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(teams.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bb18ba17-a53f-4ab7-b752-661d3a68f21a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "bf9f0b83-bca7-4888-9b11-f1213ac6a329",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year          -0.021603\n",
       "athletes       0.840817\n",
       "age            0.025096\n",
       "medals         1.000000\n",
       "prev_medals    0.920048\n",
       "Name: medals, dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams.corr(numeric_only=True)[\"medals\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7c850281-2800-4262-b16f-0a8b2cef0878",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "07bdaf3d-5272-44a4-a349-81ec02fd3ccd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x1492f506a80>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x=\"athletes\", y=\"medals\", data=teams, fit_reg=True, ci=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8c250d49-f1a8-43d6-bbe6-f99ebd8540c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x149318e34a0>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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6T07RD3pUbBtm/nz55e6GaMWi8Wm/Qf7SOj9OnJ6z46c3rMjp/fstWnhmIiISJlSSIuIiJQphfQkEg6H+eIXv0g4HC51UyYFvV9HTu/ZkdN7duT0no2eFo6JiIiUKfWkRUREypRCWkREpEwppEVERMqUQlpERKRMKaTLzIYNG3jjG99IdXU19fX1vO9972PHjh1F16RSKdavX8/MmTOpqqri4osvZt++fSVqcelt3LiRlStXFgojrFmzhnvvvbdwv96vw/va176GZVlceeWVhdv0nhX7P//n/2BZVtHXySefXLhf79fwXnnlFT760Y8yc+ZMKioqWLFiBU888UThfmMMN9xwA42NjVRUVHDuuefy4osvlrDF5UchXWaam5tZv349f/jDH3jggQdwXZfzzjuPvr6+wjVXXXUVv/rVr/jJT35Cc3Mzra2tXHTRRSVsdWnNnz+fr33tazz55JM88cQTvO1tb+O9730v27ZtA/R+Hc7jjz/Od7/7XVauXFl0u96zoZYtW0ZbW1vh63e/+13hPr1fQx08eJA3velNBINB7r33Xp577jn+6Z/+iRkzZhSuuemmm7jlllu47bbbePTRR6msrOT8888nlUqVsOVlxkhZ6+joMIBpbm42xhjT1dVlgsGg+clPflK4Zvv27QYwW7ZsKVUzy86MGTPM97//fb1fh9HT02NOOOEE88ADD5izzz7bfPrTnzbG6DM2nC9+8YvmlFNOGfY+vV/Du+aaa8xZZ5014v2+75uGhgZz8803F27r6uoy4XDY/Od//udENHFSUE+6zHV3dwNQV1cHwJNPPonrupx77rmFa04++WQWLlzIli1bStLGcuJ5HnfffTd9fX2sWbNG79dhrF+/ngsuuKDovQF9xkby4osvMnfuXBYtWsQll1zC7t27Ab1fI/nlL3/Jaaedxgc+8AHq6+t5/etfz/e+973C/bt27aK9vb3ofaupqeGMM86Y1u/bYArpMub7PldeeSVvetObWL58OQDt7e2EQiFqa2uLrp0zZw7t7e0laGV52Lp1K1VVVYTDYT75yU+yadMmli5dqvdrBHfffTdPPfUUGzZsGHKf3rOhzjjjDG6//Xbuu+8+Nm7cyK5du3jzm99MT0+P3q8RvPTSS2zcuJETTjiB+++/n3Xr1vF3f/d33HHHHQCF92bOnDlFj5vu79tgOgWrjK1f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",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x=\"age\", y=\"medals\", data=teams, fit_reg=True, ci=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "428a4998-1a5f-419e-9a0b-fdb0c9c1c4de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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AtEVt912m2677baaqgUAAMArPApElZWVWrFihbZu3arCwkJVVVW59W/btq1GigMAAKgLHgWip556SitWrFBSUpI6deokm81W03UBAADUGY8C0apVq/SXv/xFgwYNqul6AAAA6pxHH7u32+269dZba7oWAAAAr/AoED399NNauHChDMOo6XoAAADqnEePzD744ANt375d7733njp27KiAgAC3/rVr19ZIcQAAAHXBo0AUFhamhx9+uKZrAQAA8AqPAtHy5ctrug4AAACv8WgNkSRVVFRoy5Yt+v3vf68LFy5Ikk6fPq3i4uIaKw4AAKAueHSH6IsvvtCAAQOUl5en0tJS/ehHP1JwcLB+85vfqLS0VEuXLq3pOgEAAGqNR3eInnrqKfXq1Uvnzp1To0aNzPaHH35YW7durbHiAAAA6oJHd4j+8Y9/aPfu3bLb7W7tbdq00b/+9a8aKQwAAKCueHSHqKqqSpWVldXaT506peDg4BsuCgAAoC55FIgSEhK0YMECc99ms6m4uFgvvPACP+cBAADqHY8emb388stKTExUhw4ddOnSJY0YMULHjh1TixYt9Pbbb9d0jQAAALXKo0DUqlUrHTx4UKtWrVJOTo6Ki4uVnJyskSNHui2yBgAAqA88CkSS5O/vr1GjRtVkLQAAAF7hUSD605/+dM3+MWPGeFQMAACAN3gUiJ566im3/fLycl28eFF2u11BQUEEIgAAUK949Cmzc+fOuW3FxcXKzc3Vvffee12Lqnft2qXBgwcrKipKNptN69evd+s3DEMzZsxQZGSkGjVqpP79++vYsWNuY86ePauRI0cqJCREYWFhSk5OrvbzITk5Oerdu7caNmyo6OhozZ0715NpAwCAm5THv2X2be3atdOcOXOq3T26lpKSEnXt2lWLFy++av/cuXO1aNEiLV26VHv27FHjxo2VmJioS5cumWNGjhypI0eOKCMjQxs2bNCuXbs0btw4s9/lcikhIUExMTHKysrSvHnzNHPmTL3++uueTxYAANxUPF5UfdWD+fvr9OnTP3j8wIEDNXDgwKv2GYahBQsWaPr06XrwwQclXV67FBERofXr12vYsGH65z//qU2bNmnv3r3q1auXJOnVV1/VoEGD9Nvf/lZRUVFauXKlysrKtGzZMtntdnXs2FHZ2dmaP3++W3ACAADW5VEg+tvf/ua2bxiG8vPz9dprr+mee+6pkcJOnDghp9Op/v37m22hoaGKi4tTZmamhg0bpszMTIWFhZlhSJL69++vBg0aaM+ePXr44YeVmZmpPn36uP3MSGJion7zm9/o3Llzatq0abVzl5aWqrS01Nx3uVw1MicAAOCbPApEDz30kNu+zWZTy5Yt9cADD+jll1+uibrkdDolSREREW7tERERZp/T6VR4eLhbv7+/v5o1a+Y2JjY2ttoxrvRdLRClp6dr1qxZNTIPAADg+zwKRFVVVTVdh09JS0tTamqque9yuRQdHe3FigAAQG2qsUXVNc3hcEiSCgoK3NoLCgrMPofDocLCQrf+iooKnT171m3M1Y7xzXN8W2BgoEJCQtw2AABw8/LoDtE37558n/nz53tyCsXGxsrhcGjr1q3q1q2bpMt3avbs2aMJEyZIkuLj43X+/HllZWWpZ8+ekqRt27apqqpKcXFx5phf/epXKi8vV0BAgCQpIyND7du3v+rjMgAAYD0eBaIDBw7owIEDKi8vV/v27SVJn376qfz8/NSjRw9znM1mu+ZxiouL9dlnn5n7J06cUHZ2tpo1a6bWrVtr8uTJ+q//+i+1a9dOsbGx+vWvf62oqChzDdMdd9yhAQMG6IknntDSpUtVXl6uiRMnatiwYYqKipIkjRgxQrNmzVJycrKmTZumw4cPa+HChXrllVc8mToAALgJeRSIBg8erODgYL355pvmXZZz587p0UcfVe/evfX000//oOPs27dP999/v7l/5c7T2LFjtWLFCj377LMqKSnRuHHjdP78ed17773atGmTGjZsaL5m5cqVmjhxovr166cGDRpo6NChWrRokdkfGhqqzZs3KyUlRT179lSLFi00Y8YMPnIPAABMNsMwjOt90X/8x39o8+bN6tixo1v74cOHlZCQcF3fRVQfuFwuhYaGqqioqFbWE7V5bmONH7O2nZyT5O0SAAC4put5//ZoUbXL5dKZM2eqtZ85c0YXLlzw5JAAAABe41Egevjhh/Xoo49q7dq1OnXqlE6dOqW//vWvSk5O1pAhQ2q6RgAAgFrl0RqipUuX6plnntGIESNUXl5++UD+/kpOTta8efNqtEAAAIDa5lEgCgoK0u9+9zvNmzdPx48flyS1bdtWjRs3rtHiAAAA6sINfTFjfn6+8vPz1a5dOzVu3FgerM8GAADwOo8C0Vdf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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "teams.plot.hist(y=\"medals\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0051bf6b-a74c-4e75-ad03-db2b6d694f01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>1992</td>\n",
       "      <td>9</td>\n",
       "      <td>25.3</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>ALG</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>1964</td>\n",
       "      <td>7</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>AND</td>\n",
       "      <td>Andorra</td>\n",
       "      <td>1976</td>\n",
       "      <td>3</td>\n",
       "      <td>28.3</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>ANG</td>\n",
       "      <td>Angola</td>\n",
       "      <td>1980</td>\n",
       "      <td>17</td>\n",
       "      <td>17.4</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>59</th>\n",
       "      <td>ANT</td>\n",
       "      <td>Antigua and Barbuda</td>\n",
       "      <td>1976</td>\n",
       "      <td>17</td>\n",
       "      <td>23.2</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2092</th>\n",
       "      <td>VIN</td>\n",
       "      <td>Saint Vincent and the Grenadines</td>\n",
       "      <td>1988</td>\n",
       "      <td>6</td>\n",
       "      <td>20.5</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2103</th>\n",
       "      <td>YAR</td>\n",
       "      <td>North Yemen</td>\n",
       "      <td>1984</td>\n",
       "      <td>3</td>\n",
       "      <td>27.7</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2105</th>\n",
       "      <td>YEM</td>\n",
       "      <td>Yemen</td>\n",
       "      <td>1992</td>\n",
       "      <td>8</td>\n",
       "      <td>19.6</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2112</th>\n",
       "      <td>YMD</td>\n",
       "      <td>South Yemen</td>\n",
       "      <td>1988</td>\n",
       "      <td>5</td>\n",
       "      <td>23.6</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2120</th>\n",
       "      <td>ZAM</td>\n",
       "      <td>Zambia</td>\n",
       "      <td>1964</td>\n",
       "      <td>15</td>\n",
       "      <td>21.7</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>130 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team                           country  year  athletes   age  medals  \\\n",
       "19    ALB                           Albania  1992         9  25.3       0   \n",
       "26    ALG                           Algeria  1964         7  26.0       0   \n",
       "39    AND                           Andorra  1976         3  28.3       0   \n",
       "50    ANG                            Angola  1980        17  17.4       0   \n",
       "59    ANT               Antigua and Barbuda  1976        17  23.2       0   \n",
       "...   ...                               ...   ...       ...   ...     ...   \n",
       "2092  VIN  Saint Vincent and the Grenadines  1988         6  20.5       0   \n",
       "2103  YAR                       North Yemen  1984         3  27.7       0   \n",
       "2105  YEM                             Yemen  1992         8  19.6       0   \n",
       "2112  YMD                       South Yemen  1988         5  23.6       0   \n",
       "2120  ZAM                            Zambia  1964        15  21.7       0   \n",
       "\n",
       "      prev_medals  \n",
       "19            NaN  \n",
       "26            NaN  \n",
       "39            NaN  \n",
       "50            NaN  \n",
       "59            NaN  \n",
       "...           ...  \n",
       "2092          NaN  \n",
       "2103          NaN  \n",
       "2105          NaN  \n",
       "2112          NaN  \n",
       "2120          NaN  \n",
       "\n",
       "[130 rows x 7 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams[teams.isnull().any(axis=1)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5ef70841-2e95-41ed-bec3-9bde248c1adf",
   "metadata": {},
   "outputs": [],
   "source": [
    "teams = teams.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e6b3c9df-eb79-4e8d-9b7a-c8e1ef53e07c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1964</td>\n",
       "      <td>8</td>\n",
       "      <td>22.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1968</td>\n",
       "      <td>5</td>\n",
       "      <td>23.2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1972</td>\n",
       "      <td>8</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>1980</td>\n",
       "      <td>11</td>\n",
       "      <td>23.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2004</td>\n",
       "      <td>5</td>\n",
       "      <td>18.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2139</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2000</td>\n",
       "      <td>26</td>\n",
       "      <td>25.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2140</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2004</td>\n",
       "      <td>14</td>\n",
       "      <td>25.1</td>\n",
       "      <td>3</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2141</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2008</td>\n",
       "      <td>16</td>\n",
       "      <td>26.1</td>\n",
       "      <td>4</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2012</td>\n",
       "      <td>9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2016</td>\n",
       "      <td>31</td>\n",
       "      <td>27.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2014 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team      country  year  athletes   age  medals  prev_medals\n",
       "0     AFG  Afghanistan  1964         8  22.0       0          0.0\n",
       "1     AFG  Afghanistan  1968         5  23.2       0          0.0\n",
       "2     AFG  Afghanistan  1972         8  29.0       0          0.0\n",
       "3     AFG  Afghanistan  1980        11  23.6       0          0.0\n",
       "4     AFG  Afghanistan  2004         5  18.6       0          0.0\n",
       "...   ...          ...   ...       ...   ...     ...          ...\n",
       "2139  ZIM     Zimbabwe  2000        26  25.0       0          0.0\n",
       "2140  ZIM     Zimbabwe  2004        14  25.1       3          0.0\n",
       "2141  ZIM     Zimbabwe  2008        16  26.1       4          3.0\n",
       "2142  ZIM     Zimbabwe  2012         9  27.3       0          4.0\n",
       "2143  ZIM     Zimbabwe  2016        31  27.5       0          0.0\n",
       "\n",
       "[2014 rows x 7 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "b761bef1-c058-492d-8e04-dead6df595a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "train = teams[teams[\"year\"] < 2012].copy()\n",
    "test = teams[teams[\"year\"] >= 2012].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "5fd701d3-aff6-46f7-bfe0-ed7ad59f9a46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1609, 7)"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e72c388d-db64-4813-85ac-785ecd1a9ffd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(405, 7)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "e9aab82c-912c-480e-b44a-9eb61454fb1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "reg = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8d9d4c64-a28b-4512-ba50-77e5a6d4bb48",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictors = [\"athletes\", \"prev_medals\"]\n",
    "target = \"medals\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8afc985c-4873-4764-aa18-fdf6ed869c25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reg.fit(train[predictors], train[\"medals\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "25e635a2-b21d-4d8e-ab49-4be0eb703155",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = reg.predict(test[predictors])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "01809560-46b2-4464-91a9-a6664843f502",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[\"predictions\"] = predictions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "261eb8c4-c385-4c2b-8369-9ab63ebd16c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "      <th>predictions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2012</td>\n",
       "      <td>6</td>\n",
       "      <td>24.8</td>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-0.961221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2016</td>\n",
       "      <td>3</td>\n",
       "      <td>24.7</td>\n",
       "      <td>0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-1.176333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>2012</td>\n",
       "      <td>10</td>\n",
       "      <td>25.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.425032</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>2016</td>\n",
       "      <td>6</td>\n",
       "      <td>23.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.711847</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>ALG</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>2012</td>\n",
       "      <td>39</td>\n",
       "      <td>24.8</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.155629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2111</th>\n",
       "      <td>YEM</td>\n",
       "      <td>Yemen</td>\n",
       "      <td>2016</td>\n",
       "      <td>3</td>\n",
       "      <td>19.3</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.926958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2131</th>\n",
       "      <td>ZAM</td>\n",
       "      <td>Zambia</td>\n",
       "      <td>2012</td>\n",
       "      <td>7</td>\n",
       "      <td>22.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.640143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2132</th>\n",
       "      <td>ZAM</td>\n",
       "      <td>Zambia</td>\n",
       "      <td>2016</td>\n",
       "      <td>7</td>\n",
       "      <td>24.1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.640143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2012</td>\n",
       "      <td>9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.505767</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2016</td>\n",
       "      <td>31</td>\n",
       "      <td>27.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.080748</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>405 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team      country  year  athletes   age  medals  prev_medals  predictions\n",
       "6     AFG  Afghanistan  2012         6  24.8       1          1.0    -0.961221\n",
       "7     AFG  Afghanistan  2016         3  24.7       0          1.0    -1.176333\n",
       "24    ALB      Albania  2012        10  25.7       0          0.0    -1.425032\n",
       "25    ALB      Albania  2016         6  23.7       0          0.0    -1.711847\n",
       "37    ALG      Algeria  2012        39  24.8       1          2.0     2.155629\n",
       "...   ...          ...   ...       ...   ...     ...          ...          ...\n",
       "2111  YEM        Yemen  2016         3  19.3       0          0.0    -1.926958\n",
       "2131  ZAM       Zambia  2012         7  22.6       0          0.0    -1.640143\n",
       "2132  ZAM       Zambia  2016         7  24.1       0          0.0    -1.640143\n",
       "2142  ZIM     Zimbabwe  2012         9  27.3       0          4.0     1.505767\n",
       "2143  ZIM     Zimbabwe  2016        31  27.5       0          0.0     0.080748\n",
       "\n",
       "[405 rows x 8 columns]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "59b5ce89-dad3-4969-b403-78d4658613ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "test.loc[test[\"predictions\"] < 0, \"predictions\"] = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "29f557e3-adad-42c6-b59b-865b0a53a954",
   "metadata": {},
   "outputs": [],
   "source": [
    "test[\"predictions\"] = test[\"predictions\"].round()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "c5b415a3-8271-4f21-947c-e0e40037417e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "      <th>predictions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2012</td>\n",
       "      <td>6</td>\n",
       "      <td>24.8</td>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>AFG</td>\n",
       "      <td>Afghanistan</td>\n",
       "      <td>2016</td>\n",
       "      <td>3</td>\n",
       "      <td>24.7</td>\n",
       "      <td>0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>2012</td>\n",
       "      <td>10</td>\n",
       "      <td>25.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>ALB</td>\n",
       "      <td>Albania</td>\n",
       "      <td>2016</td>\n",
       "      <td>6</td>\n",
       "      <td>23.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>ALG</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>2012</td>\n",
       "      <td>39</td>\n",
       "      <td>24.8</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2111</th>\n",
       "      <td>YEM</td>\n",
       "      <td>Yemen</td>\n",
       "      <td>2016</td>\n",
       "      <td>3</td>\n",
       "      <td>19.3</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2131</th>\n",
       "      <td>ZAM</td>\n",
       "      <td>Zambia</td>\n",
       "      <td>2012</td>\n",
       "      <td>7</td>\n",
       "      <td>22.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2132</th>\n",
       "      <td>ZAM</td>\n",
       "      <td>Zambia</td>\n",
       "      <td>2016</td>\n",
       "      <td>7</td>\n",
       "      <td>24.1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2012</td>\n",
       "      <td>9</td>\n",
       "      <td>27.3</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>ZIM</td>\n",
       "      <td>Zimbabwe</td>\n",
       "      <td>2016</td>\n",
       "      <td>31</td>\n",
       "      <td>27.5</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>405 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     team      country  year  athletes   age  medals  prev_medals  predictions\n",
       "6     AFG  Afghanistan  2012         6  24.8       1          1.0          0.0\n",
       "7     AFG  Afghanistan  2016         3  24.7       0          1.0          0.0\n",
       "24    ALB      Albania  2012        10  25.7       0          0.0          0.0\n",
       "25    ALB      Albania  2016         6  23.7       0          0.0          0.0\n",
       "37    ALG      Algeria  2012        39  24.8       1          2.0          2.0\n",
       "...   ...          ...   ...       ...   ...     ...          ...          ...\n",
       "2111  YEM        Yemen  2016         3  19.3       0          0.0          0.0\n",
       "2131  ZAM       Zambia  2012         7  22.6       0          0.0          0.0\n",
       "2132  ZAM       Zambia  2016         7  24.1       0          0.0          0.0\n",
       "2142  ZIM     Zimbabwe  2012         9  27.3       0          4.0          2.0\n",
       "2143  ZIM     Zimbabwe  2016        31  27.5       0          0.0          0.0\n",
       "\n",
       "[405 rows x 8 columns]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "6c24e4df-4dd1-4729-a9e6-44e3249289c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_absolute_error\n",
    "\n",
    "error = mean_absolute_error(test[\"medals\"], test[\"predictions\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "6d9de4fb-49c4-46d7-8352-ea9cd87c34ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.2987654320987656"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b5281bc9-f133-4e83-a870-7ccbbd929506",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    2014.000000\n",
       "mean       10.990070\n",
       "std        33.627528\n",
       "min         0.000000\n",
       "25%         0.000000\n",
       "50%         0.000000\n",
       "75%         5.000000\n",
       "max       442.000000\n",
       "Name: medals, dtype: float64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teams.describe()[\"medals\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f220d7e2-d0f8-4170-90c4-c3237339931b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>team</th>\n",
       "      <th>country</th>\n",
       "      <th>year</th>\n",
       "      <th>athletes</th>\n",
       "      <th>age</th>\n",
       "      <th>medals</th>\n",
       "      <th>prev_medals</th>\n",
       "      <th>predictions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>907</th>\n",
       "      <td>IND</td>\n",
       "      <td>India</td>\n",
       "      <td>2012</td>\n",
       "      <td>95</td>\n",
       "      <td>26.0</td>\n",
       "      <td>6</td>\n",
       "      <td>3.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>908</th>\n",
       "      <td>IND</td>\n",
       "      <td>India</td>\n",
       "      <td>2016</td>\n",
       "      <td>130</td>\n",
       "      <td>26.1</td>\n",
       "      <td>2</td>\n",
       "      <td>6.0</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    team country  year  athletes   age  medals  prev_medals  predictions\n",
       "907  IND   India  2012        95  26.0       6          3.0          7.0\n",
       "908  IND   India  2016       130  26.1       2          6.0         12.0"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test[test[\"team\"] == \"IND\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f575b137-33c6-4f1d-9814-56a030b26e74",
   "metadata": {},
   "outputs": [],
   "source": [
    "errors = (test[\"medals\"] - test[\"predictions\"]).abs()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "2e6ada81-8198-4c5d-a694-e0b5dff7f748",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6       1.0\n",
       "7       0.0\n",
       "24      0.0\n",
       "25      0.0\n",
       "37      1.0\n",
       "       ... \n",
       "2111    0.0\n",
       "2131    0.0\n",
       "2132    0.0\n",
       "2142    2.0\n",
       "2143    0.0\n",
       "Length: 405, dtype: float64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "errors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "cb41350d-c3b9-4fda-9786-f8c8c36ac6db",
   "metadata": {},
   "outputs": [],
   "source": [
    "error_by_team = errors.groupby(test[\"team\"]).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "6c61db5b-1a2d-49d0-afe4-d4a28c6e35ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "team\n",
       "AFG    0.5\n",
       "ALB    0.0\n",
       "ALG    1.5\n",
       "AND    0.0\n",
       "ANG    0.0\n",
       "      ... \n",
       "VIE    1.0\n",
       "VIN    0.0\n",
       "YEM    0.0\n",
       "ZAM    0.0\n",
       "ZIM    1.0\n",
       "Length: 204, dtype: float64"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error_by_team"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c8915513-be8b-4814-83ee-753037518806",
   "metadata": {},
   "outputs": [],
   "source": [
    "medals = test[\"medals\"].groupby(test[\"team\"]).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "807cbef1-6822-4094-acc0-af9e8f68991c",
   "metadata": {},
   "outputs": [],
   "source": [
    "error_ratio = error_by_team / medals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "a9e797fa-bd53-483a-bb57-d2ca3c02bdb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "team\n",
       "AFG    1.0\n",
       "ALB    NaN\n",
       "ALG    1.0\n",
       "AND    NaN\n",
       "ANG    NaN\n",
       "      ... \n",
       "VIE    1.0\n",
       "VIN    NaN\n",
       "YEM    NaN\n",
       "ZAM    NaN\n",
       "ZIM    inf\n",
       "Length: 204, dtype: float64"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error_ratio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "1bdaf5dd-dad5-4fe0-bee6-0a0f235b46a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "team\n",
       "AFG    1.000000\n",
       "ALG    1.000000\n",
       "ARG    0.853659\n",
       "ARM    0.428571\n",
       "AUS    0.367347\n",
       "         ...   \n",
       "USA    0.126953\n",
       "UZB    0.625000\n",
       "VEN    1.750000\n",
       "VIE    1.000000\n",
       "ZIM         inf\n",
       "Length: 102, dtype: float64"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error_ratio[~pd.isnull(error_ratio)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "9f8344a2-cc78-4a7f-8155-2bebe89f80c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "error_ratio = error_ratio[np.isfinite(error_ratio)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "2f7f9613-a50c-4370-a2d0-d31fca6492e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "team\n",
       "AFG    1.000000\n",
       "ALG    1.000000\n",
       "ARG    0.853659\n",
       "ARM    0.428571\n",
       "AUS    0.367347\n",
       "         ...   \n",
       "UKR    0.951220\n",
       "USA    0.126953\n",
       "UZB    0.625000\n",
       "VEN    1.750000\n",
       "VIE    1.000000\n",
       "Length: 97, dtype: float64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error_ratio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "cab0afda-0c66-4034-88c0-484a4e19aa1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "error_ratio.plot.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "5bc4b178-f83e-4366-a5fe-96f914dbcfdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "team\n",
       "FRA    0.022472\n",
       "CAN    0.048387\n",
       "NZL    0.063492\n",
       "RUS    0.082353\n",
       "ITA    0.121429\n",
       "         ...   \n",
       "MAR    2.000000\n",
       "EGY    2.400000\n",
       "HKG    3.000000\n",
       "POR    3.333333\n",
       "AUT    4.500000\n",
       "Length: 97, dtype: float64"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error_ratio.sort_values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb10201f-f6b9-4382-9723-e6b808937b84",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
