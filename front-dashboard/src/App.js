import React, { useState, useEffect } from 'react';
import Papa from 'papaparse';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';

function App() {
  const [data, setData] = useState([]);
  const [filter, setFilter] = useState('');

  // Leitura do CSV na pasta public
  useEffect(() => {
    fetch(`${process.env.PUBLIC_URL}/dados.csv`)
      .then(res => res.text())
      .then(csvText => {
        Papa.parse(csvText, {
          header: true,
          delimiter: ';',
          complete: (results) => {
            // Converter números
            const parsed = results.data.map(row => ({
              ...row,
              irradiacao_solar: Number(row.irradiacao_solar),
              temp_painel: Number(row.temp_painel),
              temp_ambiente: Number(row.temp_ambiente),
            }));
            setData(parsed);
          },
          error: err => console.error('Erro ao processar CSV:', err),
        });
      })
      .catch(err => console.error('Erro ao buscar CSV:', err));
  }, []);

  // Filtra os dados conforme o texto digitado (em qualquer campo)
  const filteredData = data.filter(row =>
    Object.values(row).some(val =>
      String(val).toLowerCase().includes(filter.toLowerCase())
    )
  );

  const tableStyle = {
    width: '100%',
    borderCollapse: 'collapse',
    marginTop: '20px',
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    fontSize: '14px',
  };

  const thStyle = {
    borderBottom: '2px solid #333',
    padding: '10px',
    backgroundColor: '#282c34',
    color: 'white',
    textAlign: 'left',
    cursor: 'pointer',
  };

  const tdStyle = {
    borderBottom: '1px solid #ddd',
    padding: '8px',
  };

  const trHover = {
    backgroundColor: '#f5f5f5',
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Dashboard Solar - Visualização de Dados</h1>

      <input
        style={{ padding: '8px', fontSize: '16px', width: '100%', maxWidth: '400px', marginBottom: '20px' }}
        type="text"
        placeholder="Filtrar dados..."
        value={filter}
        onChange={e => setFilter(e.target.value)}
      />

      {filteredData.length > 0 ? (
        <>
          <div style={{ width: '100%', height: 300 }}>
            <ResponsiveContainer>
              <LineChart data={filteredData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="hora" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="irradiacao_solar" stroke="#8884d8" name="Irradiação Solar" />
                <Line type="monotone" dataKey="temp_painel" stroke="#82ca9d" name="Temp. Painel" />
                <Line type="monotone" dataKey="temp_ambiente" stroke="#ffc658" name="Temp. Ambiente" />
              </LineChart>
            </ResponsiveContainer>
          </div>

          <table style={tableStyle}>
            <thead>
              <tr>
                {Object.keys(filteredData[0]).map(col => (
                  <th key={col} style={thStyle}>{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {filteredData.map((row, i) => (
                <tr key={i} style={i % 2 === 1 ? trHover : undefined}>
                  {Object.values(row).map((val, j) => (
                    <td key={j} style={tdStyle}>{val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </>
      ) : (
        <p>Nenhum dado corresponde ao filtro.</p>
      )}
    </div>
  );
}

export default App;
