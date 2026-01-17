import { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [jobId, setJobId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [boxes, setBoxes] = useState<number[][]>([]);
  const [peopleCount, setPeopleCount] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const canvasRef = useRef<HTMLCanvasElement>(null);
  const imgRef = useRef<HTMLImageElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
      setBoxes([]);
      setPeopleCount(null);
      setError(null);
      setJobId(null);
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    setError(null);
    setBoxes([]);
    setPeopleCount(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "http://localhost:8000/count-people-from-uploaded",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) throw new Error(`Server error: ${response.status}`);
      const data = await response.json();
      setJobId(data.job_id);
    } catch (err: any) {
      setError(err.message || "Unknown error");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (!jobId) return;

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`http://localhost:8000/job-status/${jobId}`);
        if (!res.ok) throw new Error(`Server error: ${res.status}`);
        const data = await res.json();

        if (data.status === "DONE") {
          setPeopleCount(data.result.count);
          setBoxes(data.result.boxes);
          clearInterval(interval);
        } else if (data.error) {
          setError(data.error);
          clearInterval(interval);
        }
      } catch (err: any) {
        setError(err.message || "Unknown error");
        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [jobId]);

  const drawBoxes = () => {
    if (!canvasRef.current || !imgRef.current || boxes.length === 0) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const img = imgRef.current;
    canvas.width = img.width;
    canvas.height = img.height;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "lime";
    ctx.lineWidth = 2;

    boxes.forEach(([x1, y1, x2, y2]) => {
      const scaleX = canvas.width / img.naturalWidth;
      const scaleY = canvas.height / img.naturalHeight;

      ctx.strokeRect(
        x1 * scaleX,
        y1 * scaleY,
        (x2 - x1) * scaleX,
        (y2 - y1) * scaleY
      );
    });
  };

  useEffect(() => {
    if (imgRef.current) drawBoxes();
  }, [boxes]);


  useEffect(() => {
    if (!canvasRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    setBoxes([]);
    setPeopleCount(null);
    setError(null);
  }, [file]);

  return (
    <div className="container">
      <h1>Upload image to count people</h1>

      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file || loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {peopleCount !== null && (
        <div className="status success">
          <strong>People detected:</strong> {peopleCount}
        </div>
      )}
      {error && (
        <div className="status error">
          <strong>Error:</strong> {error}
        </div>
      )}

      {file && (
        <div className="preview" style={{ position: "relative" }}>
          <img
            ref={imgRef}
            src={URL.createObjectURL(file)}
            alt="preview"
            style={{ maxWidth: "100%", display: "block" }}
            onLoad={() => drawBoxes()}
          />
          <canvas
            ref={canvasRef}
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              pointerEvents: "none",
            }}
          />
        </div>
      )}
    </div>
  );
}

export default App;
